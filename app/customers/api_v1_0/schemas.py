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
    email: str = Field(regex=constants.EMAIL_PATTERN)
    status_code: str = Field(default=CustomerStatus.LEAD.value)

    @validator("birth_date", pre=True)
    def parse_birth_date(cls, value):
        return datetime.strptime(value, "%d/%m/%Y").date()

    class Config:
        use_enum_values = True
