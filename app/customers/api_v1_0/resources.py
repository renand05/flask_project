import json

from flask import Blueprint, request
from flask_restful import Api, Resource
from pydantic import ValidationError

from app.common import exceptions
from app.customers.api_v1_0 import schemas, tasks
from app.customers.models import Customer

customers_v1_0_bp = Blueprint("customers_v1_0_bp", __name__)

api = Api(customers_v1_0_bp)


class CustomerResource(Resource):
    def get(self):
        customers = Customer.get_all()
        return Customer.serialize_list(customers)

    def post(self):
        try:
            data = request.get_json()
            customer_input = schemas.CustomerInputSchema.parse_obj(data)
            customer = Customer(
                first_name=customer_input.first_name,
                last_name=customer_input.last_name,
                birth_date=customer_input.birth_date,
                country=customer_input.country,
                email=customer_input.last_name,
                status_code=customer_input.status_code,
                document_type=customer_input.document_type,
                document_issuing_country=customer_input.document_issuing_country,
                document_number=customer_input.document_number,
            )
            customer.save()
            tasks.create_kyc_task(customer=json.dumps(customer.serialize()))
            return customer.serialize(), 201
        except ValidationError as e:
            raise exceptions.SchemaValidationError(e)

    def put(self, id):
        try:
            data = request.get_json()
            kyc_results_input = schemas.CustomerKycTaskResultInput.parse_obj(data)
            customer = Customer.get_by_id(id)
            if kyc_results_input.kyc_final_result:
                customer.status_code = schemas.CustomerStatus.PROSPECT.value
                customer.save()
            return customer.serialize(), 200
        except ValidationError as e:
            raise exceptions.SchemaValidationError(e)


api.add_resource(CustomerResource, "/api/v1.0/customer/", endpoint="customer_resources")
api.add_resource(
    CustomerResource,
    "/api/v1.0/customer/<string:id>",
    endpoint="customer_kyc_task_update",
)
