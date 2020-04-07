#!/bin/sh
celery worker -A service.celeryconfig -n web -l info -c 2