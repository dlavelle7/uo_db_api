import django_heroku
import dj_database_url

from .settings import *

# Parse database configuration from Heroku's $DATABASE_URL (Postgres)
DATABASES = {
    'default': dj_database_url.config(conn_max_age=500, ssl_require=True)
}

# Activate Django-Heroku (DATABASE_URL and all that).
django_heroku.settings(locals())
