#!/bin/sh
sleep 25
python manage.py index --reset || true
uwsgi --ini /code/deploy/uwsgi.ini --enable-threads --disable-logging
