import pika

from app import broker


def create_kyc_task(customer):
    connection = broker.create_conn()
    channel = connection.channel()
    channel.queue_declare(queue="task_queue", durable=True)
    channel.basic_publish(
        exchange="",
        routing_key="task_queue",
        body=customer,
        properties=pika.BasicProperties(
            delivery_mode=2,  # make message persistent
        ),
    )
    connection.close()
