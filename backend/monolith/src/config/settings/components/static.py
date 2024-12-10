import os.path

from src.config.settings.components.boilerplate import BASE_DIR


STATIC_DIR = BASE_DIR

STATIC_URL = "static/"

STATIC_ROOT = os.path.join(STATIC_DIR.parent.parent, "static/")

if not os.path.exists(STATIC_ROOT):
    os.makedirs(STATIC_ROOT)

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
