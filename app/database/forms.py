forms = [
    {
        "form_name": "Client",
        "form_fields": ["name", "date registered", "email", "phone number"],
    },
    {
        "form_name": "Order", 
        "form_fields": ["description", "date created", "email"]},
    {
        "form_name": "Seller",
        "form_fields": ["name", "phone"]
    },
]


fields_types = {
    "name": "text",
    "date registered": "date",
    "email": "email",
    "phone number": "phone",
    "description": "text",
    "date created": "date",
    "phone": "phone",
}
