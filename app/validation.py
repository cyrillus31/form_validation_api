from datetime import datetime
import re

from pydantic import EmailStr 

from errors import CustomValidationError


def validate_date(d: str) -> str:
    DateValidationError = CustomValidationError(
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
        raise CustomValidationError(
            f"Invalid phone number format {p}. Use +7 XXX XXX XX XX"
        )
    return "phone"


def validate_email(email: str) -> str:
    try:
        EmailStr._validate(email)
        return email
    except ValueError:
        raise CustomValidationError("Invalid Email.")


def validate_text(text: str) -> str:
    try:
        str(text)
        return text
    except ValueError:
        raise CustomValidationError("Invalid text.")


validator_types = {
    "date": validate_date,
    "phone": validate_phone_number,
    "email": validate_email,
    "text": validate_text,
}


def validator(
    data_to_validate: str,
    validation_type: str = None,
    _validation_order = validator_types.keys(),
) -> str:
    if validation_type:
        _validation_order = [validation_type]

    for val_type in _validation_order:
        val_func = validator_types[val_type]
        try:
            val_func(data_to_validate)
            return val_type
        except CustomValidationError:
            continue
    return "Unknown"