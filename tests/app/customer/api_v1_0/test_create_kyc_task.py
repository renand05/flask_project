from mock import patch
import pika
from app.customers.api_v1_0 import tasks

def test_create_a_kyc_task(app):
    with app.test_client() as test_client:
        with patch.object(pika, "BlockingConnection"):
            tasks.create_kyc_task({"test":"test"})