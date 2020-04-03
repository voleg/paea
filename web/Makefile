start_web:
	uwsgi --ini deploy/uwsgi.ini --enable-threads

start_worker:
	 celery worker -A service.celeryconfig -n web -l debug -c 4
