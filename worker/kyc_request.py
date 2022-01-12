import pydantic
import random
import asyncio

class _Settings(pydantic.BaseSettings):
    url_legal_service = "https://test.com"
    url_id_service = "https://test2.com"


"""simple request mocks for external kyc records and verifications"""
class KycServicesClient:
    _SETTINGS = _Settings()

    @classmethod
    async def check_customer_id(cls, customer_id):
        await asyncio.sleep(5)
        return random.choice([True, False])

    @classmethod
    async def check_customer_judicial_records(cls, customer_id):
        await asyncio.sleep(8)
        return random.choice([True, False])