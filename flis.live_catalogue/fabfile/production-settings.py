
HOSTNAME = "http://projects.eionet.europa.eu/flis-services-project/live-catalogue"
FORCE_SCRIPT_NAME = '/flis-services-project/live-catalogue'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'live_catalogue',                      # Or path to database file if using sqlite3.
        'USER': 'edw',                      # Not used with sqlite3.
        'PASSWORD': 'edw',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}
FRAME_URL = 'http://projects.eionet.europa.eu/flis-services-project/flis_templates/frame'
FRAME_COOKIES = ['__ac', '_ZopeId']
MEDIA_ROOT = '/var/local/naaya/live_catalogue/instance'

MEDIA_URL = '/flis-services-project/live-catalogue/static/files/'

ASSETS_DEBUG = True
ALLOWED_HOSTS = ['localhost', '*']
USE_X_FORWARDED_HOST = True
STATIC_URL = HOSTNAME + '/static/'
DEBUG = False
ASSETS_ROOT = '/var/local/naaya/live_catalogue/live_catalogue/live_catalogue/static'
