from celery import Celery, signature
from flask import Flask, jsonify

app = Flask(__name__)
cel = Celery(app.name, broker="amqp://guest:guest@rabbitmq")


@app.route("/test", methods=["POST"])
def test():
    task = signature("add", args=(2, 3))
    res = task.delay()

    return jsonify({"task": {"id": res.id}})
