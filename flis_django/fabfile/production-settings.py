from path import path

HOSTNAME = "http://projects.eionet.europa.eu/flis-services-project/flis"
FORCE_SCRIPT_NAME = '/flis-services-project/flis'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'flis',                      # Or path to database file if using sqlite3.
        'USER': 'edw',                      # Not used with sqlite3.
        'PASSWORD': 'edw',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}
FRAME_URL = 'http://projects.eionet.europa.eu/flis-services-project/flis_templates/frame'
FRAME_COOKIES = ['__ac', '_ZopeId']
MEDIA_ROOT = path('/var/local/naaya/flis/instance')
MEDIA_URL = '/static/files'
ASSETS_DEBUG = True
USE_X_FORWARDED_HOST = True
STATIC_URL = HOSTNAME + '/static/'
