#!/bin/bash

cd /src

celery -A src.celery_app.app worker -l info --concurrency=2