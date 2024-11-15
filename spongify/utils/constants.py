# Base Spongify Constants
from dotenv import dotenv_values


class UtilsExceptions:
    """Spongify Utils Exceptions"""


class AppNames:
    """Spongify App Names"""

    ACCOUNTS = "accounts"


class SpogifySettings:
    """Spongify Settings Constants"""

    config = dotenv_values(".env")
    SECRET_KEY = config.get("SECRET_KEY")
    ROOT_URL = "spongify.urls"
    DATABASE = config.get("DJANGO_DATABASE_URL")
    ALLOWED_HOSTS = config.get("ALLOWED_HOSTS")
    AUTH_USER_MODEL = "accounts.User"
    LANGUAGE_CODE = "en-us"
    TIME_ZONE = "Asia/Kolkata"
    STATIC_URL = "static/"
    STATICFILES_DIRS = "templates/static/"
    STATIC_ROOT = "assets/"
    MEDIA_URL = "media/"
    MEDIA_ROOT = "media"
    DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
    DEBUG_TOOLBAR_IP = "127.0.0.1"
    TEMPLATE = "templates"


class EmailConfig:
    """Email Configurations"""

    config = dotenv_values(".env")
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = "smtp.gmail.com"
    PORT_587 = 587
    PORT_465 = 465
    EMAIL_HOST_USER = config.get("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = config.get("EMAIL_HOST_PASSWORD")


class CeleryConfig:
    """Celery Configurations"""

    config = dotenv_values(".env")
    BROKER_URL = config.get("CELERY_BROKER_URL")
    CELERY_RESULT_BACKEND = "redis"
    CELERY_ACCEPT_CONTENT = ["application/json"]
    CELERY_TASK_SERIALIZER = "json"
    CELERY_RESULT_SERIALIZER = "json"
    CELERY_TIMEZONE = "Asia/Kolkata"
    CELERY_ENABLE_UTC = True
