import os.path

from src.config.settings.components.static import STATIC_DIR


MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(STATIC_DIR, "media/")
