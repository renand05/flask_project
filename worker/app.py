import json

import asyncio
import pika
import random
import time

sleepTime = 20
time.sleep(sleepTime)

connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq"))
channel = connection.channel()
channel.queue_declare(queue="task_queue", durable=True)


class CustomerKycClient:
    def __init__(self, customer_id):
        self.customer_id = customer_id

    @asyncio.coroutine
    async def is_customer_id_valid_in_national_registry_system(self):
        await asyncio.sleep(1)
        return random.choice([True, False])

    @asyncio.coroutine
    async def has_customer_any_judicial_records(self):
        await asyncio.sleep(5)
        return random.choice([True, False])

    def can_customer_be_prospect(self, result_1, result_2):
        if result_1 and result_2:
            return random.choice([True, False])
        return False

    def check_kyc_rules(self):
        tasks = (
            self.is_customer_id_valid_in_national_registry_system(),
            self.has_customer_any_judicial_records(),
        )
        loop = asyncio.get_event_loop()
        result_1, result_2 = loop.run_until_complete(asyncio.gather(*tasks))
        result_3 = self.can_customer_be_prospect(result_1, result_2)
        loop.close()
        return result_1, result_2, result_3


def callback(ch, method, properties, body):
    customer_dict = json.loads(body.decode())
    customer_id = customer_dict.get("id")
    kyc_client = CustomerKycClient(customer_id=customer_id)
    result_1, result_2, result_3 = kyc_client.check_kyc_rules()
    print("=========result===========", result_1, result_2, result_3)
    # TODO send request with kyc results
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue="task_queue", on_message_callback=callback)
channel.start_consuming()
