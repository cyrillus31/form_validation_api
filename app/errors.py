from pydantic import ValidationError 


class CustomValidationError(Exception):
    def __init__(self, message: str, errors=None):
        super().__init__(message)
        self.errors = errors
