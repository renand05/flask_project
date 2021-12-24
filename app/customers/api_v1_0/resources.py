from flask import request, Blueprint
from flask_restful import Api, Resource

from app.common.exceptions import ObjectNotFound
from app.customers.api_v1_0.schemas import CustomerSchema
from app.customers.models import Customer

customers_v1_0_bp = Blueprint("customers_v1_0_bp", __name__)

customer_schema = CustomerSchema()

api = Api(customers_v1_0_bp)


class CustomerResource(Resource):
    def get(self):
        customers = Customer.get_all()
        result = customer_schema.dump(customers, many=True)
        return result

    def post(self):
        data = request.get_json()
        customer_dict = customer_schema.load(data)
        customer = Customer(
            first_name=customer_dict["first_name"],
            last_name=customer_dict["last_name"],
            birth_date=customer_dict["birth_date"],
            email=customer_dict["email"],
        )
        customer.save()
        resp = customer_schema.dump(customer)
        return resp, 201


api.add_resource(CustomerResource, "/api/v1.0/customer/", endpoint="customer_resource")
