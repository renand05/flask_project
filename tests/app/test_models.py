import datetime


def test__create_user(database):
    from app.customers.models import Customer

    customer = Customer(
        first_name="Tom",
        last_name="Hanks",
        birth_date=datetime.datetime(1986, 2, 19),
        country="CO",
        status_code="LEAD",
        email="tom@gmail.com",
        document_type="CC",
        document_issuing_country="CO",
        document_number="12345678",
    )
    database.session.add(customer)
    database.session.commit()
