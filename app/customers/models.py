from app.db import db, BaseModelMixin


class Customer(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    birth_date = db.Column(db.String)
    email = db.Column(db.String)

    def __init__(self, first_name, last_name, birth_date, email):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.email = email

    def __repr__(self):
        return f"Customer({self.first_name} {self.last_name})"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
