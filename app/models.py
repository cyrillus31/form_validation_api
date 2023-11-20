import datetime
import re

from pydantic import BaseModel, EmailStr, validator, create_model

def validate_date(cls, d):
    try:
        valid_date = datetime.datetime.strptime(d, "%d.%m.%Y")
    except ValueError:
        try:
            valid_date = datetime.datetime.strptime(d, "%Y-%m-%d")
        except ValueError:
            raise cls.DateValueError
    return valid_date

def validate_phone_number(cls, p):
    pattern = r'\+7\s\d{3}\s\d{3}\s\d{2}\s\d{2}'
    if not re.match(pattern, p):
        raise ValueError(f"Invalid phone number format {p}. Use +7 XXX XXX XX XX")
    return p

class Config:
    arbitrary_types_allowed = True

def ValidationModelFactory(**kwargs):
    _val = {}
    for field in kwargs:
        if kwargs[field] == "phone":
            _val["phone"] = _val.get("phone", []) + [filed]
        elif kwargs[field] == "date":
            _val["date"] = _val.get("date", []) + [field]

    FormModel = create_model(FormModel, **kwargs, __validators__={})


class BaseForm(BaseModel):
    date: str | None
    phone: str | None
    email: EmailStr | None

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





