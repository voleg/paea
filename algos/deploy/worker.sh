#!/bin/sh
celery worker -A service.celeryconfig -n algos@%h -l info -c 2
