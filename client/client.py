from celery import Celery
from celery.result import AsyncResult
from flask import Flask, jsonify
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)
cel = Celery("client",
                backend="db+postgresql://root:pass@postgres/root",
                broker="amqp://guest:guest@rabbitmq")

cel.conf.task_routes = {
    '*': {'queue': 'foobar'},
}

pending = []

@app.route("/test", methods=["GET"])
def test():
    task = cel.signature('add', args=(2, 3))
    app.logger.info(f"Task is: {task}")
    res = task.delay()
    pending.append(res.id)

    return jsonify({"task": {"id": res.id}})

@app.route("/task/<uuid>", methods=["GET"])
def get_task(uuid):
    result = AsyncResult(uuid, app=cel)
    r = result.get()
    app.logger.info(result)
    return jsonify({
        'task_uuid': uuid,
        'result_value': r,
        'result': result.state
    })