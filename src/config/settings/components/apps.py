import os
import sys

from config.settings.components.boilerplate import BASE_DIR
import environ

env = environ.Env()
environ.Env.read_env(BASE_DIR / '.env')

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
    # Ninja
    "ninja_extra",
    "ninja_jwt",
    # "ninja-schema",
]

if env("USE_ELASTIC") == 1:
    THIRD_PARTY += [
        # Elastic
        "elasticapm.contrib.django",
    ]

sys.path.insert(0, os.path.join(BASE_DIR, "apps"))


LOCAL_APPS = [
    "src.apps.chats.apps.ChatsConfig",
    "src.apps.notes.apps.NotesConfig",
    "src.apps.quizzes.apps.QuizzesConfig",
    "src.apps.sources.apps.SourcesConfig",
    "src.apps.students.apps.StudentsConfig",
    "src.apps.words.apps.WordsConfig",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY + LOCAL_APPS
