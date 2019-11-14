FROM python:3.7-slim

RUN apt update && \
    apt install -y libpq-dev gcc && \
    pip install pipenv

COPY Pipfile* /tmp/
RUN cd /tmp && pipenv lock --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY . /app/

USER 1000:1000
WORKDIR /app
CMD celery worker -A app.app -Q foobar -P solo -E -l info