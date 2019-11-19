# celery-test

Example application demonstrating Celery distributed work queues.

## Usage

Fire the whole thing up with `docker-compose up`.

You can then access the following services:

- http://localhost:5000/add/`a`/`b` - submit a new `add` task (which fails if `a=2`)
- http://localhost:5000/task/`uuid` - fetch the result for task with given UUID
- http://localhost:5000/task/async/`uuid` - inspect the async result for task with given UUID
- http://localhost:5000/task/abort/`uuid` - abort task with given UUID (killing the Celery worker in the process)
- http://localhost:5555 - the Flower web interface
- http://localhost:8888 - the PgAdmin4 web interface (user: `root@example.org`, pass: `pass`)
- http://localhost:16572 - the RabbitMQ web interface (user: `guest`, pass: `guest`)