from contextlib import nullcontext
from app.app import handler

def test_handler():
    event = {
                "first_name": "John",
                "last_name": "Smith"
            }
    output = handler(event, nullcontext)

    assert output["message"] == "Hello John Smith!"