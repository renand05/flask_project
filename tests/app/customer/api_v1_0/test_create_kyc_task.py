import pika


def test_create_a_kyc_task(task_conn):
    channel = task_conn.channel()
    channel.queue_declare(queue="task_queue", durable=True)
    channel.basic_publish(
        exchange="",
        routing_key="task_queue",
        body="test",
        properties=pika.BasicProperties(
            delivery_mode=2,  # make message persistent
        ),
    )
