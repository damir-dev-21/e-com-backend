from pathlib import Path
import config


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-12w04+_hfp(^h)5d5+o=^3ly7yml@$+sp-fv0b*kg@ho3rsk)3'

DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
    '10.0.2.2',
    '94.103.83.34'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config.DATABASE,
        'USER': config.PGUSER,
        'PASSWORD': config.PGPASSWORD,
        'HOST': config.DBHOST,
        'PORT': config.PORT,
    }
}
