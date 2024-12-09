import environ

from src.config.settings.components.boilerplate import BASE_DIR


env = environ.Env()
environ.Env.read_env(BASE_DIR / '.env')


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('POSTGRES_DB'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': env('POSTGRES_HOST'),
        'PORT': env('POSTGRES_PORT'),
    },
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
