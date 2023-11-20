from datetime import datetime
import re

from pydantic import ValidationError
from database.db import find_forms_by_fields


def validate_date(d):
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


def validate_phone_number(p):
    pattern = r"\+7\s\d{3}\s\d{3}\s\d{2}\s\d{2}"
    if not re.match(pattern, p):
        raise ValidationError(f"Invalid phone number format {p}. Use +7 XXX XXX XX XX")
    return "phone"


