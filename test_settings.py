from crp.settings import *
# this import is actually necessary

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'changeme',
        'HOST': 'db',
        'PORT': '5432',
    }
}
