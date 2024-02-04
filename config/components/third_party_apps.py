INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


# -------------------------------------------------------------------
# grapelli (personalización de site admin) debe ir antes de cualquier otra app
# -------------------------------------------------------------------
# INSTALLED_APPS = ['grappelli'] + INSTALLED_APPS


# -------------------------------------------------------------------
# configuración para django-crispy-forms
# -------------------------------------------------------------------
INSTALLED_APPS += ['crispy_forms','crispy_bootstrap4']
CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap4'
CRISPY_TEMPLATE_PACK = 'bootstrap4'


# -------------------------------------------------------------------
# configuración para django-table
# -------------------------------------------------------------------
INSTALLED_APPS += ['django_tables2',]


# -------------------------------------------------------------------
# configuración para django-table
# -------------------------------------------------------------------
INSTALLED_APPS += ['django_filters',]


# -------------------------------------------------------------------
# configuración para django-select2
# -------------------------------------------------------------------
INSTALLED_APPS += ['django_select2']


# # -------------------------------------------------------------------
# # configuración para django-smart-selects
# # -------------------------------------------------------------------
# INSTALLED_APPS += ['smart_selects',]
# # JQUERY_URL = True
# USE_DJANGO_JQUERY = True


# -------------------------------------------------------------------
# configuración para debug
# -------------------------------------------------------------------
if DEBUG:
    INSTALLED_APPS += ['debug_toolbar',]
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware',]
    INTERNAL_IPS = ['localhost', '127.0.0.1', '172.19.0.1']  # gateway del docker
    DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False,}


# -------------------------------------------------------------------
# autenticación personalizada
# -------------------------------------------------------------------
INSTALLED_APPS += ['core.authentication',]
