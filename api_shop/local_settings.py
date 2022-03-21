from pathlib import Path
import config


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-2wd04+_hfp(^h)5d5+o=^3ly7yml@$+hp-fv0b*kg@ho3rsk)3'

DEBUG = True

ALLOWED_HOSTS = [

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

