import time

from celery import Celery
from celery import signals

from tqdm import trange

app = Celery("worker",
             backend="db+postgresql://root:pass@postgres/root",
             broker="amqp://guest:guest@rabbitmq")

app.conf.task_routes = {
    '*': {'queue': 'foobar'},
}


@signals.worker_ready.connect
def worker_ready_callback(sender=None, *args, **kwargs):
    print(f'Worker ready: {sender}')

    for arg in args:
        print(f'\t{arg}')

    for k, v in kwargs.items():
        print(f'\t{k}={v}')


@signals.worker_shutdown.connect
def worker_shutdown_callback(sender=None, *args, **kwargs):
    print(f'Worker shutting down: {sender}')

    for arg in args:
        print(f'\t{arg}')

    for k, v in kwargs.items():
        print(f'\t{k}={v}')


@signals.task_sent.connect
def task_sent_callback(sender=None, *args, **kwargs):
    print(f'Task sent: {sender}')

    for arg in args:
        print(f'\t{arg}')

    for k, v in kwargs.items():
        print(f'\t{k}={v}')


@signals.task_success.connect
def task_success_callback(sender=None, *args, **kwargs):
    print(f'Task success: {sender}')

    for arg in args:
        print(f'\t{arg}')

    for k, v in kwargs.items():
        print(f'\t{k}={v}')


@signals.task_failure.connect
def task_failure_callback(sender=None, *args, **kwargs):
    print(f'Task failure: {sender}')

    for arg in args:
        print(f'\t{arg}')

    for k, v in kwargs.items():
        print(f'\t{k}={v}')


class AddTask(app.Task):
    name = "add"

    def run(self, a, b):
        if a == 2:
            raise ValueError("Cannot add to 2")

        print(f"Calculating {a}+{b}")
        for i in trange(100):
            self.update_state(state='THINKING', meta={
                'progress': i
            })
            time.sleep(0.25)

        return a + b


app.register_task(AddTask())
