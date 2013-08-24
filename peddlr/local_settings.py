DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Local Django settings for hondemand project.

import os
gettext = lambda s: s
#PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))


INTERNAL_IPS = ('127.0.0.1',)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'hackathon',                      # Or path to database file if using sqlite3.
        'USER': 'root',
        'PASSWORD': 'resdev',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}


# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: '/Users/rypalmer/Sites/ookaportal/ookaportal/media/'
MEDIA_ROOT = '/Users/andrewdrake/Sites/static/hackathon/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: '/Users/rypalmer/Sites/ookaportal/ookaportal/static_root'
STATIC_ROOT = '/Users/andrewdrake/Sites/static/hackathon/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    '/Users/andrewdrake/Sites/peddlr//peddlr/static',
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    '/Users/andrewdrake/Sites/peddlr///templates',
)

CDN_MEDIA_PREFIX = ''