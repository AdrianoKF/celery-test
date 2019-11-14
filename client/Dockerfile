FROM python:3.7-slim

RUN apt update && \
    apt install -y libpq-dev gcc && \
    pip install pipenv

COPY Pipfile* /tmp/
RUN cd /tmp && pipenv lock --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt

VOLUME /app
COPY . /app/

EXPOSE 5000
USER 1000:1000
WORKDIR /app
# CMD celery worker -A app -Q test -l info
# CMD python client.py
ENV FLASK_APP client.py
CMD ["sh", "start.sh"]