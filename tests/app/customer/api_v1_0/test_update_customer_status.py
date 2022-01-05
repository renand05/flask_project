from mock import patch
import datetime
from app.customers.models import Customer

_PAYLOAD_SUCCESFUL_REQUEST = {
    "is_customer_id_valid_in_national_registry_system": "True",
    "has_customer_any_judicial_records": "False",
    "can_customer_be_prospect": 0.8,
}


_PAYLOAD_INVALID_FORMAT_REQUEST = {}

_CUSTOMER_MOCK = Customer(
    first_name="Tom",
    last_name="Hanks",
    birth_date=datetime.datetime(1986,2,19),
    country="CO",
    status_code="LEAD",
    email="tom@gmail.com",
    document_type="CC",
    document_issuing_country="CO",
    document_number="12345678",
)


def test__should_update_customer_status(app):
    from app.customers.api_v1_0 import tasks
    from app.customers.models import Customer

    with app.test_client() as test_client:
        with patch.object(Customer, "save") as save_in_db:
            with patch.object(Customer, "get_by_id") as get_by_id:
                save_in_db.return_value = None
                get_by_id.return_value = _CUSTOMER_MOCK
                rv = test_client.put(
                    "/api/v1.0/customer/1", json=_PAYLOAD_SUCCESFUL_REQUEST
                )
                assert rv.status_code == 200


def test__should_raise_error_when_invalid_format_given_to_update_customer(app):
    from app.customers.models import Customer

    with app.test_client() as test_client:
        with patch.object(Customer, "save") as save_in_db:
            with patch.object(Customer, "get_by_id") as get_by_id:
                save_in_db.return_value = None
                get_by_id.return_value = _CUSTOMER_MOCK
                rv = test_client.put(
                    "/api/v1.0/customer/1", json=_PAYLOAD_INVALID_FORMAT_REQUEST
                )
                assert rv.status_code == 400
