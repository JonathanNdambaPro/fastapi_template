FROM python:3.8-slim-buster

ENV BUCKECT_NAME="sknow-gcs-landing-eu-dv"

WORKDIR /app
COPY . /app

RUN pip3 install -r requirements.txt

CMD gunicorn main:app -c gunicorn_config.py