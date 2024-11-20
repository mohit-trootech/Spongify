from os import path
import dj_database_url
from pathlib import Path
from utils.constants import EmailConfig
from utils.constants import CeleryConfig
from utils.constants import SpogifySettings as Settings


# APPEND_SLASH -  Append slash to the end of URLs
# =====================================================
APPEND_SLASH = True

# BASE_DIR - Project ROOT Directory Path Reference
# =====================================================
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
# =====================================================
SECRET_KEY = Settings.SECRET_KEY


# AUTH_USER_MODEL - Targets the custom user model
AUTH_USER_MODEL = Settings.AUTH_USER_MODEL

# ROOT_URLCONF - URL dispatcher
ROOT_URLCONF = Settings.ROOT_URL

# Admins -
ADMINS = [
    ("mohit prajapat", "mohit.prajapat@trootech.com"),
]
MANAGERS = ADMINS

# INSTALLED_APPS - Registery for installed applications
# =====================================================
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
AUTH_APPS = [
    "spongify",
    "accounts.apps.AccountsConfig",
    "library.apps.LibraryConfig",
    "music.apps.MusicConfig",
]
THIRD_PARTY_APPS = [
    "django_extensions",
    "phonenumber_field",
    "dj_database_url",
    "login_required",
    "debug_toolbar",
    "schema_graph",
]
INSTALLED_APPS = DJANGO_APPS + AUTH_APPS + THIRD_PARTY_APPS


# MIDDLEWARE - hooks into Django's request/response processing.
# =====================================================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "login_required.middleware.LoginRequiredMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

# TEMPLATES - HTML files placeholder
# CONTEXT_PRCESSORS - data to templates always
# =====================================================
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [path.join(BASE_DIR, Settings.TEMPLATE)],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# Ignore Paths for Login Required
# =====================================================
LOGIN_REQUIRED_IGNORE_PATHS = [
    "/accounts/login/$",
    "/accounts/register/$",
    "/accounts/password-reset/$",
    "/accounts/password-reset-done/$",
    "/admin/$",
    "/about/$",
]


# WSGI Configuration
# =====================================================
WSGI_APPLICATION = "spongify.wsgi.application"

# Database
# =====================================================
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
DATABASES = {}
DATABASES["default"] = dj_database_url.parse(Settings.DATABASE)

# AUTH_PASSWORD_VALIDATORS - Password validations scopes
# =====================================================
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# =====================================================
# https://docs.djangoproject.com/en/5.1/topics/i18n/
LANGUAGE_CODE = Settings.LANGUAGE_CODE
TIME_ZONE = Settings.TIME_ZONE
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# =====================================================
# https://docs.djangoproject.com/en/5.1/howto/static-files/
STATIC_URL = Settings.STATIC_URL
STATICFILES_DIRS = [path.join(BASE_DIR, Settings.STATICFILES_DIRS)]
STATIC_ROOT = Settings.STATIC_ROOT

# Media files (CSS, JavaScript, Images)
# =====================================================
MEDIA_URL = Settings.MEDIA_URL
MEDIA_ROOT = path.join(BASE_DIR, Settings.MEDIA_ROOT)


# Default primary key field type
# =====================================================
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = Settings.DEFAULT_AUTO_FIELD


# Email Configuration
# =====================================================
EMAIL_BACKEND = EmailConfig.EMAIL_BACKEND
EMAIL_HOST = EmailConfig.EMAIL_HOST
EMAIL_USE_SSL = True  # use port 465
EMAIL_USE_TLS = False  # use port 587
EMAIL_PORT = EmailConfig.PORT_465 if EMAIL_USE_SSL else EmailConfig.PORT_587
EMAIL_HOST_USER = EmailConfig.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = EmailConfig.EMAIL_HOST_PASSWORD


# Django Debug Toolbar Configuration
# =====================================================
INTERNAL_IPS = [Settings.DEBUG_TOOLBAR_IP]
DEBUG_TOOLBAR_PANELS = [
    "debug_toolbar.panels.history.HistoryPanel",
    "debug_toolbar.panels.versions.VersionsPanel",
    "debug_toolbar.panels.timer.TimerPanel",
    "debug_toolbar.panels.settings.SettingsPanel",
    "debug_toolbar.panels.headers.HeadersPanel",
    "debug_toolbar.panels.request.RequestPanel",
    "debug_toolbar.panels.sql.SQLPanel",
    "debug_toolbar.panels.staticfiles.StaticFilesPanel",
    "debug_toolbar.panels.templates.TemplatesPanel",
    "debug_toolbar.panels.alerts.AlertsPanel",
    "debug_toolbar.panels.cache.CachePanel",
    "debug_toolbar.panels.signals.SignalsPanel",
    "debug_toolbar.panels.redirects.RedirectsPanel",
    "debug_toolbar.panels.profiling.ProfilingPanel",
]

# Celery Configurations
CELERY_BROKER_URL = CeleryConfig.BROKER_URL
CELERY_RESULT_BACKEND = CeleryConfig.CELERY_RESULT_BACKEND
CELERY_ACCEPT_CONTENT = CeleryConfig.CELERY_ACCEPT_CONTENT
CELERY_TASK_SERIALIZER = CeleryConfig.CELERY_TASK_SERIALIZER
CELERY_RESULT_SERIALIZER = CeleryConfig.CELERY_RESULT_SERIALIZER
CELERY_RESULT_EXTENDED = True
CELERY_TIMEZONE = CeleryConfig.CELERY_TIMEZONE
CELERY_ENABLE_UTC = CeleryConfig.CELERY_ENABLE_UTC


# Logging Configuration - Log only data I wanted to log in project
# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "formatters": {
#         "verbose": {
#             "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
#             "style": "{",
#         },
#         "simple": {
#             "format": "{levelname} {message}",
#             "style": "{",
#         },
#     },
#     "handlers": {
#         "file": {
#             "level": "DEBUG",
#             "class": "logging.FileHandler",
#             "filename": "debug.log",
#             "formatter": "verbose",
#         },
#     },
#     "loggers": {
#         "django": {
#             "handlers": ["file"],
#             "level": "DEBUG",
#             "propagate": True,
#         },
#         "utils": {
#             "handlers": ["file"],
#             "level": "DEBUG",
#             "propagate": True,
#         },
#         "accounts": {
#             "handlers": ["file"],
#             "level": "DEBUG",
#             "propagate": True,
#         },
#     },
# }
