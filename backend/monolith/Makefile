ENV = --env-file .env
LOGS = docker logs
EXEC = docker exec -it
APP_CONTAINER = django
WORKER_1_CONTAINER = celery_worker_1
WORKER_2_CONTAINER = celery_worker_2
WORKER_3_CONTAINER = celery_worker_3
WORKER_4_CONTAINER = celery_worker_4
WORKER_BEAT_CONTAINER = celery_beat
REDIS_CONTAINER = redis
NGINX_CONTAINER = nginx
DB_CONTAINER = postgres
DC = docker compose
MANAGE_PY = python manage.py
NETWORK_NAME = backend


.PHONY: check-network up-all up-all-no-cache up-all-2 up-django up-django-db up-django-db-pgadmin-adminer up-pgadmin up-db up-adminer down-all down-all-2 down-django down-django-db down-pgadmin down-db down-adminer migrations superuser test collectstatic logs-django logs-worker-1 logs-worker-2 logs-worker-beat logs-redis logs-nginx logs-db logs-pgadmin logs-adminer logs-all

check-network:
	@echo "Checking for network $(NETWORK_NAME)..."
	@if ! docker network ls | grep -q $(NETWORK_NAME); then \
		echo "Network $(NETWORK_NAME) does not exist. Creating..."; \
		docker network create $(NETWORK_NAME); \
	else \
		echo "Network $(NETWORK_NAME) already exists."; \
	fi

up-all: check-network
	$(DC) -f docker_compose/db/docker-compose.yml $(ENV) up -d
	$(DC) -f docker_compose/django/docker-compose.yml $(ENV) up -d
	$(DC) -f docker_compose/pgadmin/docker-compose.yml $(ENV) up -d
	$(DC) -f docker_compose/adminer/docker-compose.yml $(ENV) up -d

up-all-no-cache: check-network
	$(DC) -f docker_compose/db/docker-compose.yml $(ENV) build --no-cache
	$(DC) -f docker_compose/django/docker-compose.yml $(ENV) build --no-cache
	$(DC) -f docker_compose/pgadmin/docker-compose.yml $(ENV) build --no-cache
	$(DC) -f docker_compose/adminer/docker-compose.yml $(ENV) build --no-cache
	$(DC) -f docker_compose/db/docker-compose.yml $(ENV) up -d
	$(DC) -f docker_compose/django/docker-compose.yml $(ENV) up -d
	$(DC) -f docker_compose/pgadmin/docker-compose.yml $(ENV) up -d
	$(DC) -f docker_compose/adminer/docker-compose.yml $(ENV) up -d

up-all-2:
	$(DC) -f docker_compose/db/docker-compose.yml \
	      -f docker_compose/django/docker-compose.yml \
	      -f docker_compose/pgadmin/docker-compose.yml \
	      -f docker_compose/adminer/docker-compose.yml \
	      $(ENV) up -d

up-django:
	$(DC) -f docker_compose/django/docker-compose.yml $(ENV) up -d

up-django-db:
	$(DC) -f docker_compose/db/docker-compose.yml $(ENV) up -d
	$(DC) -f docker_compose/django/docker-compose.yml $(ENV) up -d

up-django-db-pgadmin-adminer:
	$(DC) -f docker_compose/db/docker-compose.yml $(ENV) up -d
	$(DC) -f docker_compose/django/docker-compose.yml $(ENV) up -d
	$(DC) -f docker_compose/pgadmin/docker-compose.yml $(ENV) up -d
	$(DC) -f docker_compose/adminer/docker-compose.yml $(ENV) up -d

up-pgadmin:
	$(DC) -f docker_compose/pgadmin/docker-compose.yml $(ENV) up -d

up-db:
	$(DC) -f docker_compose/db/docker-compose.yml $(ENV) up -d

up-adminer:
	$(DC) -f docker_compose/adminer/docker-compose.yml $(ENV) up -d

down-all:
	$(DC) -f docker_compose/db/docker-compose.yml down
	$(DC) -f docker_compose/django/docker-compose.yml down
	$(DC) -f docker_compose/pgadmin/docker-compose.yml down
	$(DC) -f docker_compose/adminer/docker-compose.yml down

down-all-2:
	$(DC) -f docker_compose/db/docker-compose.yml \
	      -f docker_compose/django/docker-compose.yml \
	      -f docker_compose/pgadmin/docker-compose.yml \
	      -f docker_compose/adminer/docker-compose.yml \
	      down

down-django:
	$(DC) -f docker_compose/django/docker-compose.yml down

down-django-db:
	$(DC) -f docker_compose/db/docker-compose.yml down
	$(DC) -f docker_compose/django/docker-compose.yml down

down-pgadmin:
	$(DC) -f docker_compose/pgadmin/docker-compose.yml down

down-db:
	$(DC) -f docker_compose/db/docker-compose.yml down

down-adminer:
	$(DC) -f docker_compose/adminer/docker-compose.yml down

migrations:
	$(EXEC) $(APP_CONTAINER) ${MANAGE_PY} makemigrations

migrate:
	$(EXEC) $(APP_CONTAINER) ${MANAGE_PY} migrate

superuser:
	$(EXEC) $(APP_CONTAINER) sh -c ' PYTHONPATH=/app/src:$$PYTHONPATH ${MANAGE_PY} createsuperuser'

test:
	$(EXEC) $(APP_CONTAINER) ${MANAGE_PY} test

collectstatic:
	$(EXEC) $(APP_CONTAINER) sh -c ' PYTHONPATH=/app/src:$$PYTHONPATH ${MANAGE_PY} collectstatic --noinput'

logs-django:
	$(LOGS) $(APP_CONTAINER)

logs-worker-1:
	$(LOGS) $(WORKER_1_CONTAINER)

logs-worker-2:
	$(LOGS) $(WORKER_2_CONTAINER)

logs-worker-beat:
	$(LOGS) $(WORKER_BEAT_CONTAINER)

logs-redis:
	$(LOGS) $(REDIS_CONTAINER)

logs-nginx:
	$(LOGS) $(NGINX_CONTAINER)

logs-db:
	$(LOGS) $(DB_CONTAINER)

logs-pgadmin:
	$(LOGS) $(PGADMIN_CONTAINER)

logs-adminer:
	$(LOGS) $(ADMINER_CONTAINER)

logs-all: logs-django logs-worker-1 logs-worker-2 logs-worker-beat logs-redis logs-nginx logs-db logs-pgadmin logs-adminer