FROM python:3.7.4-alpine

RUN pip3 install -U pip setuptools
RUN pip3 install uwsgi

ENV DJANGO_SETTINGS_MODULE app.settings

COPY requirements.txt /pandora/requirements.txt
RUN pip3 install -r /pandora/requirements.txt

ADD . /code
WORKDIR /code

# Remove develop settings from production image
RUN rm -rf deploy/settings_dev.conf

ENTRYPOINT ["celery", "-A", "service.celeryconf", "-n" "web", "-l", "debug", "-c", "4"]
