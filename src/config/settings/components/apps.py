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
    # DCRF
    "channels",
    # DRF
    "rest_framework",
    "rest_framework.authtoken",
    "rest_framework_simplejwt",
    "django_extensions",
    "drf_yasg",
    # Cache
    "cachalot",
    # Elastic
    "elasticapm.contrib.django",
    # Ninja
    "ninja_extra",
    "ninja_jwt",
    # "ninja-schema",
]

sys.path.insert(0, os.path.join(BASE_DIR, "apps"))


LOCAL_APPS = [
    "src.apps.words.apps.WordsConfig",
    "src.apps.chats.apps.ChatsConfig",
    "src.apps.sources.apps.SourcesConfig",
    "src.apps.notes.apps.NotesConfig",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY + LOCAL_APPS
