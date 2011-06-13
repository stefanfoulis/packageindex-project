from .project import *
import os

here = lambda * x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)
PROJECT_ROOT = here('..', '..')
DATA_ROOT = here('..', '..', 'local')
project_root = lambda * x: os.path.join(os.path.abspath(PROJECT_ROOT), *x)
data_root = lambda * x: os.path.join(os.path.abspath(DATA_ROOT), *x)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': data_root('database.sqlite3'),
    }
}

MEDIA_ROOT = '/Users/Shared/PyPi-Mirror/'#data_root('uploads','media')
MEDIA_URL = '/media/'

STATIC_ROOT = data_root('collectstatic')
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'
STATICFILES_DIRS = (
    project_root('static'),
)

SECRET_KEY = '+552k_oz9pxsmf&1lp_iahgwm#pysxekmve4g)j94vox4caoyz'