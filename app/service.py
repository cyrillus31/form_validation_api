from validation import form_fits
from database.db import find_forms_by_fields, add_types


test_fields = ["name", "date registered", "phone number", "email"]
test_recieved_form = {
    "name": "kirill",
    "date registered": "1993-07-31",
    "phone number": "+7 915 111 11 11",
    "email": "kirill.olegovich31@gmail.com"
}

form_that_fits = find_forms_by_fields(*test_fields)[0]
form_that_fits_with_types = add_types(form_that_fits)

print(form_that_fits_with_types)

form_name = form_fits(test_recieved_form, form_that_fits_with_types)



print(form_name)
