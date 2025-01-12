MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'src.apps.common.middlewares.ElasticApmMiddleware',
    # 'elasticapm.contrib.django.middleware.TracingMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'src.apps.common.middlewares.DBLoggingMiddleware',
]
