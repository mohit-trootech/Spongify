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


class FormsClasses:
    """Custom Classes for Forms"""

    INPUT = "input text-black bg-white input-primary input-sm input-bordererd w-full"
    PASSWORD_INPUT = "input text-black bg-white input-primary input-sm input-bordererd w-full password-toggle"
    INPUT = "input text-black bg-white input-primary input-sm input-bordererd w-full"
    TEXT_AREA = "textarea textarea-primary textarea-sm textarea-bordererd w-full"
    TOGGLE = "toggle toggle-primary toggle-sm "
    SELECT = (
        "select text-black bg-white select-primary select-sm select-bordererd w-full"
    )
    IMAGE_INPUT = (
        "file-input text-black bg-white file-input-bordered file-input-primary w-full"
    )
    # Otp Classes
    OTP_CLASS = "w-14 h-14 text-center text-2xl font-extrabold text-slate-900 bg-slate-100 border border-slate-900 hover:border-slate-200 appearance-none rounded p-4 outline-none focus:bg-white focus:border-indigo-400 focus:ring-2 focus:ring-indigo-100 focus:ring-opacity"
