FROM python:3.7-alpine

RUN pip install pipenv

COPY Pipfile* /tmp/
RUN cd /tmp && pipenv lock --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY . /app/

EXPOSE 5000
USER 1000:1000
WORKDIR /app
# CMD celery worker -A app -Q test -l info
# CMD python client.py
ENV FLASK_APP client.py
CMD flask run --host=0.0.0.0