
HOSTNAME = 'http://projects.eionet.europa.eu/flis-services-project/live-catalogue'
ALLOWED_HOSTS = ['localhost', '*']
USE_X_FORWARDED_HOST = True
FORCE_SCRIPT_NAME = '/flis-services-project/live-catalogue'
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'live_catalogue',
        'USER': 'edw',
        'PASSWORD': 'edw',
    }
}

FRAME_URL = 'http://projects.eionet.europa.eu/flis-services-project/flis_templates/frame'
FRAME_COOKIES = ['__ac', '_ZopeId']

STATIC_URL = HOSTNAME + '/static/'
MEDIA_ROOT = '/var/local/naaya/live_catalogue/instance'
MEDIA_URL = '/flis-services-project/live-catalogue/static/files/'
ASSETS_DEBUG = True

