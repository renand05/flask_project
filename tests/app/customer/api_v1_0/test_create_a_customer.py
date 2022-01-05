from mock import patch

_PAYLOAD_SUCCESFUL_REQUEST = {
    "first_name": "Tom",
    "last_name": "Hanks",
    "birth_date": "12/12/1969",
    "country": "CO",
    "email": "tom@gmail.com",
    "document_type": "CC",
    "document_issuing_country": "CO",
    "document_number": "12345678",
}

_PAYLOAD_INVALID_FORMAT_REQUEST = {
    "first_name": "Tom",
    "last_name": "Hanks",
    "birth_date": 24234343,
    "country": "CO",
    "email": "tom@gmail.com",
    "document_type": "CC",
    "document_issuing_country": "CO",
    "document_number": "12345678",
}


def test__should_create_a_new_customer(app):
    from app.customers.api_v1_0 import tasks
    from app.customers.models import Customer

    with app.test_client() as test_client:
        with patch.object(Customer, "save") as save_in_db:
            with patch.object(tasks, "create_kyc_task") as kyc_task:
                save_in_db.return_value = None
                kyc_task.return_value = None
                rv = test_client.post(
                    "/api/v1.0/customer/", json=_PAYLOAD_SUCCESFUL_REQUEST
                )
                assert rv.status_code == 201
                kyc_task.assert_called_once()
                save_in_db.assert_called_once()


def test__should_raise_error_when_invalid_format_given_to_create_customer(app):
    from app.customers.api_v1_0 import tasks
    from app.customers.models import Customer

    with app.test_client() as test_client:
        with patch.object(Customer, "save") as save_in_db:
            with patch.object(tasks, "create_kyc_task") as kyc_task:
                save_in_db.return_value = None
                kyc_task.return_value = None
                rv = test_client.post(
                    "/api/v1.0/customer/", json=_PAYLOAD_INVALID_FORMAT_REQUEST
                )
                assert rv.status_code == 400
