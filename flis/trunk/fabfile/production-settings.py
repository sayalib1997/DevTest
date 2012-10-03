from path import path

instance_path = path(__file__).parent

secret_key_path = instance_path/'secret_key.txt'
if secret_key_path.isfile():
    SECRET_KEY = secret_key_path.text().strip()

HTABLES_ENGINE = 'postgresql'
HTABLES_POSTGRESQL_URI = "postgresql://edw:edw@localhost/flis"
FRAME_URL = 'http://projects.eionet.europa.eu/flis-services-project/flis_templates/frame'
USER_FILES_PATH = "instance/files"
FILE_SIZE_LIMIT_MB = 10