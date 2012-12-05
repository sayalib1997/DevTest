from path import path

HOSTNAME = "http://projects.eionet.europa.eu/flis-services-project/mk"
FORCE_SCRIPT_NAME = '/flis-services-project/mk/'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'flis_mk',                      # Or path to database file if using sqlite3.
        'USER': 'edw',                      # Not used with sqlite3.
        'PASSWORD': 'edw',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}
FRAME_URL = 'http://projects.eionet.europa.eu/flis-services-project/flis_templates/frame'
FRAME_COOKIES = ['__ac', '_ZopeId']
MEDIA_ROOT = path('/var/local/naaya/flis_countries/mk/instance')
MEDIA_URL = '/static/files'
ASSETS_DEBUG = True
USE_X_FORWARDED_HOST = True

#instance_path = path(__file__).parent
#
#secret_key_path = instance_path/'secret_key.txt'
#if secret_key_path.isfile():
#    SECRET_KEY = secret_key_path.text().strip()

