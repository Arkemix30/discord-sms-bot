import json


def serialize_number_addresses(numbers: list[str]):
    binding_list = [
        json.dumps({"binding_type": "sms", "address": number})
        for number in numbers
    ]
    return binding_list
