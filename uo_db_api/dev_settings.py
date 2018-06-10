from .settings import *

# Overwrite dev settings here . . .
DEBUG = True

# sqlite db instead of postgres
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
