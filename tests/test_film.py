from mock import Mock, patch
import json
import pytest


def test__should_create_a_new_customer(app):
    from app.customers.models import Customer

    payload = {
        "first_name": "Tom",
        "last_name": "Hanks",
        "birth_date": "2021/12/12",
        "email": "tom@gmail.com",
    }
    with app.test_client() as test_client:
        with patch.object(Customer, "save") as save_in_db:
            save_in_db.return_calue = None
            rv = test_client.post("/api/v1.0/customer/", json=payload)
            assert rv.status_code == 201
