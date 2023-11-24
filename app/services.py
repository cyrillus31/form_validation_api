from form import Form


def evaluate_form(recieved_form: dict) -> dict | str:
    form = Form(recieved_form)
    name = form.find_name()
    if name == "Unknown":
        return form.fields_with_types
    return name
