forms = [
    {
        "form_name": "Client",
        "form_fields": ["client name", "date registered", "client email", "phone number"],
    },
    {
        "form_name": "Order", 
        "form_fields": ["order description", "date created", "customer email"]},
    {
        "form_name": "Seller",
        "form_fields": ["seller name", "phone number"]
    },
]


fields_types = {
    "client name": "text",
    "seller name": "text",
    "order description": "text",
    "date registered": "date",
    "date created": "date",
    "client email": "email",
    "customer email": "email",
    "phone number": "phone",
}
