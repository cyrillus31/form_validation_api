from validation import form_fits, find_types
from database.db import find_forms_by_fields, add_types


test_fields = ["name", "date registered", "phone number", "email"]
test_recieved_form = {
    "name": "kirill",
    "date registered": "31.07.1993",
    "phone number": "+7 915 111 11 11",
    "email": "kirill.olegovich31@gmail.com"
}


def find_forms_with_same_fields(recieved_form: dict) -> dict | None:
    """Returns a form from a database that covers the same fields"""
    _fields = recieved_form.keys()
    form_that_fits = find_forms_by_fields(*_fields)
    if len(form_that_fits) > 1:
        return None
    form_that_fits_with_types = add_types(form_that_fits[0])
    return form_that_fits_with_types

# print(form_that_fits_with_types)


def check_types_fit(recieved_form: dict, form_that_fits: dict) -> str | None:
    form_name = form_fits(recieved_form, form_that_fits)
    if form_name:
        return form_name
    return None


def evaluate_form(recieved_form: dict) -> dict | str:
    form_that_fits = find_forms_with_same_fields(recieved_form)
    if not form_that_fits:
        return "No specific form can be idetified."
    form_name = check_types_fit(recieved_form, form_that_fits)
    if form_name:
        return form_name
    unknow_form_with_types = find_types(recieved_form)
    return unknow_form_with_types



if __name__ == "__main__":
    result = evaluate_form(recieved_form=test_recieved_form)
    print(result)


