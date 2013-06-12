from fabric.api import *
from fabric.contrib.files import *
from path import path as ppath

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
    'user': 'edw',
})


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
def install_flis():
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
    run("%s/bin/python %s/manage.py loaddata countries" % (app['sandbox'],
                                                           app['repo']))

@task
def flis_supervisor():
    run("'%(sandbox)s/bin/supervisord'" % {
            'sandbox': app['sandbox'],
        })

@task
def update_flis():
    _svn_repo(app['repo'], app['flis-repo'], update=True)

    if not exists(app['sandbox']):
        run("virtualenv --distribute '%(sandbox)s'" % app)
    run("%(sandbox)s/bin/pip install -r %(repo)s/requirements.txt" % app)

    put(app['localrepo']/'fabfile'/'production-settings.py',
        str(app['flis_var']/'local_settings.py'))

    upload_template(app['localrepo']/'fabfile'/'supervisord.conf',
                    str(app['sandbox']/'supervisord.conf'),
                    context=app, backup=False)

    run("%s/bin/python %s/manage.py syncdb" % (app['sandbox'], app['repo']))
    run("%s/bin/python %s/manage.py migrate" % (app['sandbox'], app['repo']))

    execute('service_flis', 'restart')


@task
def service_flis(action):
    run("'%(sandbox)s/bin/supervisorctl' %(action)s %(name)s" % {
            'sandbox': app['sandbox'],
            'action': action,
            'name': 'flis',
        })

@task
def deploy_flis():
    execute('install_flis')
    execute('flis_supervisor')
    execute('service_flis', 'restart')

