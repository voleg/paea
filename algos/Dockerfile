FROM python:3.7.5-alpine3.10
# RUN apk --update add --no-cache g++

# debian
# FROM python:3.7
# RUN pip install -U --timeout 1000 pip setuptools && apt-get update -qq
LABEL authors="Oleg Sapunov <ffrooty@gmail.com>"

COPY requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt

ADD . /code
WORKDIR /code

# Remove develop settings from production image
RUN rm -rf deploy/settings_dev.conf

RUN python setup.py install

CMD 'deploy/worker.sh'
