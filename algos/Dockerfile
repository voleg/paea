FROM python:3.7
LABEL authors="Oleg Sapunov <ffrooty@gmail.com>"

RUN pip install -U --timeout 1000 pip setuptools && apt-get update -qq

# COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt

ADD . /code
WORKDIR /code

# Remove develop settings from production image
RUN rm -rf deploy/settings_dev.conf

RUN python setup.py install

ENTRYPOINT ["celery", "worker", "-A", "service.celeryconfig", "-l", "info", "-n", "algos@%h"]
