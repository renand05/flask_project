from mock import patch

_PAYLOAD_SUCCESFUL_REQUEST = {
    "first_name": "Tom",
    "last_name": "Hanks",
    "birth_date": "12/12/1969",
    "email": "tom@gmail.com",
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
