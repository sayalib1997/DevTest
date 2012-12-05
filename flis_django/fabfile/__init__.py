from fabric.api import *
from fabric.contrib.files import *
from path import path as ppath

country_codes = ['pt', 'cz', 'be', 'ro', 'at', 'ir', 'sk', 'hu', 'me', 'mk',
                 'al', 'xk']

app = env.app = {
    'flis-repo': 'https://svn.eionet.europa.eu/repositories/Python/flis_django',
    'localrepo': ppath(__file__).abspath().parent.parent,
}

try: from localcfg import *
except: pass

app.update({
    'instance_var': app['repo']/'instance',
    'flis_var': app['repo']/'flis',
    'sandbox': app['repo']/'sandbox',
    'countries_sandbox': app['countries_repo']/'sandbox',
    'user': 'edw',
})

for country_code in country_codes:
    app['%s-instance_var' % country_code] = '%s/%s/instance' % (
                                        app['countries_repo'], country_code)
    app['%s-flis_var' % country_code] = '%s/%s/flis' % (
                                        app['countries_repo'], country_code)

@task
def ssh():
    open_shell("cd '%(repo)s'" % app)


def _install_random_key(remote_path, key_length=20, mode=0600):
    import random
    import string
    from StringIO import StringIO
    vocabulary = string.ascii_letters + string.digits
    key = ''.join(random.choice(vocabulary) for c in xrange(key_length))
    put(StringIO(key), remote_path, mode=mode)


def _svn_repo(repo_path, origin_url, update=True):
    if not exists(repo_path/'.svn'):
        run("mkdir -p '%s'" % repo_path)
        with cd(repo_path):
            run("svn co '%s' ." % origin_url)

    elif update:
        with cd(repo_path):
            run("svn up")

@task
def install():
    _svn_repo(app['repo'], app['flis-repo'], update=True)

    if not exists(app['sandbox']):
        run("virtualenv --distribute '%(sandbox)s'" % app)
    run("%(sandbox)s/bin/pip install -r %(repo)s/requirements.txt" % app)

    if not exists(app['instance_var']):
        run("mkdir -p '%(instance_var)s'" % app)
    if not exists(app['instance_var']/'files'):
        run("mkdir -p '%(instance_var)s/files'" % app)

    secret_key_path = app['instance_var']/'secret_key.txt'
    if not exists(secret_key_path):
        _install_random_key(str(secret_key_path))

    put(app['localrepo']/'fabfile'/'production-settings.py',
        str(app['flis_var']/'local_settings.py'))

    upload_template(app['localrepo']/'fabfile'/'supervisord.conf',
                    str(app['sandbox']/'supervisord.conf'),
                    context=app, backup=False)

    run("%s/bin/python %s/manage.py syncdb" % (app['sandbox'], app['repo']))
    run("%s/bin/python %s/manage.py migrate" % (app['sandbox'], app['repo']))

@task
def install_countries():
    for country_code in country_codes:
        _svn_repo(app['countries_repo']/country_code, app['flis-repo'], update=True)

        if not exists(app['%s-instance_var' % country_code]):
            run("mkdir -p %s" % app['%s-instance_var'] % country_code)
        if not exists('%s/files' % app['%s-instance_var' % country_code]):
            run("mkdir -p %s/files" % app['%s-instance_var' % country_code])

        secret_key_path = '%s/secret_key.txt' % app['%s-instance_var' % country_code]
        if not exists(secret_key_path):
            _install_random_key(str(secret_key_path))

        put(app['localrepo']/'fabfile'/'production-settings-%s.py' % country_code,
            '%s/local_settings.py' % app['%s-flis_var' % country_code])

    upload_template(app['localrepo']/'fabfile'/'countries-supervisord.conf',
                    str(app['countries_sandbox']/'supervisord.conf'),
                    context=app, backup=False)

    if not exists(app['countries_sandbox']):
        run("virtualenv --distribute '%(countries_sandbox)s'" % app)
    run("%(countries_sandbox)s/bin/pip install -r %(countries_repo)s/pt/requirements.txt" % app)


    for country_code in country_codes:
        run("%s/bin/python %s/manage.py syncdb" % (
                        app['countries_sandbox'], '%s/%s' % 
                            (app['countries_repo'], country_code)
                        )
            )
        run("%s/bin/python %s/manage.py migrate" % (
                        app['countries_sandbox'], '%s/%s' %
                            (app['countries_repo'], country_code)
                        )
            )

@task
def service(action):
    run("'%(sandbox)s/bin/supervisorctl' %(action)s %(name)s" % {
            'sandbox': app['sandbox'],
            'action': action,
            'name': 'flis_django',
        })

@task
def countries_service(action):
    for country_code in country_codes:
        run("'%(sandbox)s/bin/supervisorctl' %(action)s %(name)s" % {
                'sandbox': app['countries_sandbox'],
                'action': action,
                'name': 'flis_%s' % country_code,
            })

@task
def deploy():
    execute('install')
    execute('service', 'restart')

@task
def deploy_countries():
    execute('install_countries')
    execute('countries_service', 'restart')

@task
def restart_countries():
    execute('countries_service', 'restart')

@task
def stop_countries():
    execute('countries_service', 'stop')

