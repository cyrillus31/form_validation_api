from datetime import datetime
import re

from pydantic import EmailStr, ValidationError
from database.db import find_forms_by_fields, add_types, fields_types


def validate_date(d: str) -> str:
    DateValidationError = ValidationError(
        "Invalid date format. Use DD.MM.YYYY or YYYY-MM-DD"
    )
    try:
        valid_date = datetime.strptime(d, "%d.%m.%Y")
    except ValueError:
        try:
            valid_date = datetime.strptime(d, "%Y-%m-%d")
        except ValueError:
            raise DateValidationError
    return "date"


def validate_phone_number(p: str) -> str:
    pattern = r"\+7\s\d{3}\s\d{3}\s\d{2}\s\d{2}"
    if not re.match(pattern, p):
        raise ValidationError(f"Invalid phone number format {p}. Use +7 XXX XXX XX XX")
    return "phone"

def validate_email(email: str) -> str: 
    try:
        EmailStr.validate(email)
        return email
    except ValueError:
        raise ValidationError("Invalid Email.")


def validate_text(text: str) -> str:
    try:
        str(text)
        return text
    except ValueError:
        raise ValidationError("Invalid text.")

validator_types = {
        "data": validate_date,
        "phone": validate_phone_number,
        "email": validate_email,
        "text": validate_text
        }

def validator(data_to_validate: str, validation_type: str = None, _validation_order: list[str] = validator_types.keys()) -> str | bool:
    if validation_type:
        _validation_order = [validation_type]

    for val_type in _validation_order:
        val_func = validator_types[val_type]
        try:
            val_func(data_to_validate)
            return val_type
        except ValidationError:
            continue
    return False 



def form_fits(recieved_form: dict, form_to_validate_by: dict):
    forms_fit = True 
    for field in form_to_validate_by:
        t = form_to_validate_by[field]


    if ... :

        return form_to_validate_by["form_name"]
    else:
        return False

