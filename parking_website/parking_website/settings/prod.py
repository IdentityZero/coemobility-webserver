from .base import *
import json

with open('/etc/web_server_config.json', 'r') as config_file:
    config = json.load(config_file)

SECRET_KEY = config['SECRET_KEY']
DEBUG = True

ALLOWED_HOSTS = ['47.129.54.22', 'localhost', 'coemobility.com']

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": config["DB_NAME"],
        "USER" : config["DB_USER"],
        "PASSWORD": config["DB_PASSWORD"],
        "HOST": config["DB_HOST"],
        "PORT": 3306,
    }
}

CORS_ALLOWED_ORIGINS = [
    'http://47.129.54.22',
    'https://47.129.54.22',
    'http://localhost',
    'https://coemobility.com',
]

AWS_ACCESS_KEY_ID = config['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = config['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = config['AWS_STORAGE_BUCKET_NAME']
AWS_STORAGE_BUCKET_NAME_THUMBNAILS = config['AWS_STORAGE_BUCKET_NAME_THUMBNAILS']
AWS_S3_SIGNATURE_NAME = config['AWS_S3_SIGNATURE_NAME']
AWS_S3_REGION_NAME = config['AWS_S3_REGION_NAME']
AWS_S3_FILE_OVERWRITE = config['AWS_S3_FILE_OVERWRITE']
AWS_DEFAULT_ACL = config['AWS_DEFAULT_ACL']
AWS_S3_VERITY = config['AWS_S3_VERITY']
DEFAULT_FILE_STORAGE = config['DEFAULT_FILE_STORAGE']

THUMBNAIL_BUCKET_URL = config['THUMBNAIL_BUCKET_URL'] % AWS_STORAGE_BUCKET_NAME_THUMBNAILS

DATA_SERVER_URL = config['DATA_SERVER_URL'] # Used for API calls set to ''