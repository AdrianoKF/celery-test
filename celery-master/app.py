from .celery import Celery

app = Celery("worker",
                backend="db+postgresql://root:pass@postgres/root",
                broker="amqp://guest:guest@rabbitmq")

app.conf.task_routes = {
    '*': {'queue': 'foobar'},
}

@app.task(name="add")
def add(a, b):
    print(f"Calculating {a}+{b}")
    return a + b
