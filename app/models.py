import datetime
import re

from pydantic import BaseModel, EmailStr, validator


class BaseForm(BaseModel):
    date: str
    phone: str

    DateValueError = ValueError("Invalid date format. Use DD.MM.YYYY or YYYY-MM-DD")

    @validator("date")
    def validate_date(cls, d):
        try:
            valid_date = datetime.datetime.strptime(d, "%d.%m.%Y")
        except ValueError:
            try:
                valid_date = datetime.datetime.strptime(d, "%Y-%m-%d")
            except ValueError:
                raise cls.DateValueError
        return valid_date

    @validator("phone")
    def validate_phone_number(cls, p):
        pattern = r'\+7\s\d{3}\s\d{3}\s\d{2}\s\d{2}'
        if not re.match(pattern, p):
            raise ValueError(f"Invalid phone number format {p}. Use +7 XXX XXX XX XX")
        return p

    class Config:
        arbitrary_types_allowed = True




class NewForm(BaseForm):
    # form_title: str
    name: str
    phone: str
    email: EmailStr
    date: str





