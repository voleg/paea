FROM python:3.7.5-alpine3.10
RUN apk --update add --no-cache uwsgi uwsgi-python3

# DEBIAN
# FROM python:3.7
# RUN pip install -U --timeout 1000 pip setuptools && apt-get update -qq
# RUN pip3 install uwsgi

ENV DJANGO_SETTINGS_MODULE service.settings

COPY requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt

ADD . /code
WORKDIR /code

# Remove develop settings from production image
RUN rm -rf deploy/settings_dev.conf

CMD 'deploy/start_web_server.sh'
