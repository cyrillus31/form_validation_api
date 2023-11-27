import json

import requests

endpoint = "get_form"
url = f"http://form-validation-api.fvds.ru/{endpoint}"
localhost = f"http://127.0.0.1:8000/{endpoint}"

choice = input(
    f"""Do you want to send test requests to localhost(1) or to the remote server(2)? 1/2: """
)


if choice == "1":
    url = localhost

print(f"POST requests will be sent to {url}\n")

headers = {"Content-Type": "application/x-www-form-urlencoded"}

test_data = [
    # Valid forms with extra fields
    {
        "client name": "Kirill",
        "client email": "kirill.olegovich31@gmail.com",
        "phone number": "+7 123 456 78 91",
        "date registered": "19.04.2023",
        "sports": "bjj",
    },
    {
        "order description": "Macitosh",
        "date created": "1984-01-24",
        "customer email": "steve.jobs@apple.com",
        "motto": "Think different",
    },
    {
        "seller name": "Microsoft",
        "phone number": "+7 916 619 69 96",
        "founder": "Bill Gates",
    },
    # Invalid forms
    {"company": "Yandex", "country of origin": "Russia", "founded": "1997-09-23"},
    {
        "courier name": "Grigory",
        "courier email": "Grigory.olegovich31@gmail.com",
        "phone number": "+9123456",
        "date registered": "04.19.2023",
        "sports": "2023-11-22",
        "model description": "Lisa",
        "date created": "1984-01-24",
        "customer email": "steve.wozniak@apple.com",
        "motto": "If I had asked my customers what they wanted they would have said a faster horse.",
    },
    {
        "client name": "Kirill",
        "client email": "kirill.com",
        "phone number": "+7 123 456 78 91",
        "date registered": "19.04.2023",
        "sports": "bjj",
    },
]


def show_request_body_sent(data: dict) -> None:
    request = requests.Request(
        data=data, method="POST", url=url, headers=headers
    ).prepare()
    print("Request body:", request.body, "\n")


def prettify_json(json_string: str) -> str:
    return json.dumps(json.loads(json_string), indent=4)


for index, test in enumerate(test_data, 1):
    print(f"\nTest #{index}\n")
    show_request_body_sent(data=test)

    response = requests.post(url, data=test)
    response_body = prettify_json(response.text)

    print("Response body:", response_body)

