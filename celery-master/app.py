from celery import Celery

app = Celery(__name__, broker="amqp://guest:guest@rabbitmq//")


@app.task(name="add")
def add(a, b):
    return a + b
