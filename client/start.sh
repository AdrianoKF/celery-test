#!/bin/sh

flask run --host=0.0.0.0
# celery worker -A client.cel -Q foobar -P solo -l info