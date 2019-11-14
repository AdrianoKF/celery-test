FROM python:3.7-alpine

RUN pip install pipenv

COPY Pipfile* /tmp/
RUN cd /tmp && pipenv lock --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY . /app/

USER 1000:1000
WORKDIR /app
CMD celery worker -A app -l info