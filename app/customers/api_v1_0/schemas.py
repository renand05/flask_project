from datetime import date, datetime

import enum
from pydantic import BaseModel, Field, validator

from app.common import constants


class CustomerStatus(enum.Enum):
    LEAD = "LEAD"
    PROSPECT = "PROSPECT"


class CustomerInputSchema(BaseModel):
    first_name: str
    last_name: str
    birth_date: date
    country: str
    email: str = Field(regex=constants.EMAIL_PATTERN)
    status_code: str = Field(default=CustomerStatus.LEAD.value)
    document_type: str
    document_issuing_country: str
    document_number: str

    @validator("birth_date", pre=True)
    def parse_birth_date(cls, value):
        return datetime.strptime(value, "%d/%m/%Y").date()

    class Config:
        use_enum_values = True


class CustomerKycTaskResultInput(BaseModel):
    is_customer_id_valid_in_national_registry_system: str
    has_customer_any_judicial_records: str
    can_customer_be_prospect: int
    kyc_final_result: bool = False

    @validator("kyc_final_result", always=True)
    def are_kyc_results_fulfilled(cls, kyc_final_result, values):
        return values.get("can_customer_be_prospect") > 0.7
