FROM python:3.7-alpine

RUN pip install pipenv

COPY Pipfile* /tmp/
RUN cd /tmp && pipenv lock --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt

EXPOSE 5555
USER 1000:1000
WORKDIR /app
CMD celery flower --broker=amqp://guest:guest@rabbitmq