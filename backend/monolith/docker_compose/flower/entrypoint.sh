#!/bin/bash

# celery -A src.celery_app.app --broker=${CELERY_BROKER_URL} flower --port=5555
celery -A src.celery_app.app flower --port=5555 --broker=${CELERY_BROKER_URL}