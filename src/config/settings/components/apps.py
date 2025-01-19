import os
import sys

from config.settings.components.boilerplate import BASE_DIR


DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY = [
    "channels",
    "rest_framework",
    "rest_framework.authtoken",
    "rest_framework_simplejwt",
    "django_extensions",
    "drf_yasg",
    "cachalot",
    "elasticapm.contrib.django",
]

sys.path.insert(0, os.path.join(BASE_DIR, "apps"))


LOCAL_APPS = [
    "src.apps.words.apps.WordsConfig",
    "src.apps.chats.apps.ChatsConfig",    
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY + LOCAL_APPS
