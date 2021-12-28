from app.db import BaseModelMixin, db


class Customer(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    birth_date = db.Column(db.Date)
    country = db.Column(db.String)
    email = db.Column(db.String)
    status_code = db.Column(db.String)
    document_type = db.Column(db.String)
    document_issuing_country = db.Column(db.String)
    document_number = db.Column(db.String)

    def __init__(
        self,
        first_name,
        last_name,
        birth_date,
        country,
        email,
        status_code,
        document_type,
        document_issuing_country,
        document_number,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.country = country
        self.email = email
        self.status_code = status_code
        self.document_type = document_type
        self.document_issuing_country = document_issuing_country
        self.document_number = document_number

    def __repr__(self):
        return f"Customer({self.first_name} {self.last_name})"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def serialize(self):
        customer_dict = self.serializer()
        customer_dict["birth_date"] = customer_dict.get("birth_date").strftime(
            "%d/%m/%Y"
        )
        return customer_dict

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]
