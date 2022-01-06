import pika


def create_conn():
    return pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq"))
