import json

import asyncio
import pika
import random
import requests
import time
import kyc_request

sleepTime = 20
time.sleep(sleepTime)

connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq"))
channel = connection.channel()
channel.queue_declare(queue="task_queue", durable=True)

loop = asyncio.get_event_loop()
_KYC_CLIENT = kyc_request.KycServicesClient()

class CustomerKycClient:
    def __init__(self, customer_id):
        self.customer_id = customer_id

    @asyncio.coroutine
    async def is_customer_id_valid_in_national_registry_system(self):
        return _KYC_CLIENT.check_customer_id(customer_id=self.customer_id)

    @asyncio.coroutine
    async def has_customer_any_judicial_records(self):
        return _KYC_CLIENT.check_customer_judicial_records(customer_id=self.customer_id)

    def can_customer_be_prospect(self, is_id_valid, has_legal_records):
        random_results = [0.1, 0.5] * 5 + [0.6, 0.7] * 5 + [0.8, 1] * 90
        kyc_result = 0
        if is_id_valid and not has_legal_records:
            kyc_result = random.choice(random_results)
        return kyc_result

    def check_kyc_rules(self):
        tasks = (
            self.is_customer_id_valid_in_national_registry_system(),
            self.has_customer_any_judicial_records(),
        )
        is_id_valid, has_legal_records = loop.run_until_complete(asyncio.gather(*tasks))
        kyc_result = self.can_customer_be_prospect(
            is_id_valid=is_id_valid, has_legal_records=has_legal_records
        )
        return is_id_valid, has_legal_records, kyc_result


def kyc_result_response(customer_id, is_valid_id, has_legal_records, kyc_result):
    headers = {"Content-Type": "application/json"}
    requests.put(
        url=f"http://web:5000/api/v1.0/customer/{customer_id}",
        data=json.dumps(
            {
                "is_customer_id_valid_in_national_registry_system": is_valid_id,
                "has_customer_any_judicial_records": has_legal_records,
                "can_customer_be_prospect": kyc_result,
            }
        ),
        headers=headers,
    )


def callback(ch, method, properties, body):
    customer_dict = json.loads(body.decode())
    customer_id = customer_dict.get("id")
    kyc_client = CustomerKycClient(customer_id=customer_id)
    is_id_valid, has_legal_records, kyc_result = kyc_client.check_kyc_rules()
    kyc_result_response(
        customer_id=customer_id,
        is_valid_id=is_id_valid,
        has_legal_records=has_legal_records,
        kyc_result=kyc_result,
    )
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue="task_queue", on_message_callback=callback)
channel.start_consuming()
loop.close()
