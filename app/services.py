from validation import form_fits, find_types
from database.db import find_forms_by_fields, add_types


def find_forms_with_same_fields(recieved_form: dict) -> dict | None:
    """Returns a form from a database that covers the same fields"""
    _fields = recieved_form.keys()
    forms_that_fit = find_forms_by_fields(*_fields)
    amount_correct_forms = len(forms_that_fit)
    if amount_correct_forms == 0 or amount_correct_forms > 1:
        return None
    form_that_fits_with_types = add_types(forms_that_fit[0])
    return form_that_fits_with_types


def check_types_fit(recieved_form: dict, form_that_fits: dict) -> str | None:
    form_name = form_fits(recieved_form, form_that_fits)
    if form_name:
        return str(form_name)
    return None


def evaluate_form(recieved_form: dict) -> dict | str:
    form_that_fits = find_forms_with_same_fields(recieved_form)
    if form_that_fits:
        form_name = check_types_fit(recieved_form, form_that_fits)
        if form_name:
            return form_name
    unknow_form_with_types = find_types(recieved_form)
    return unknow_form_with_types
