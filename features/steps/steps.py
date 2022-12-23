import requests
from behave import then, when


@when("I request a ping")
def request_ping(context):
    context.response = requests.get("http://localhost:8080/ping", timeout=2)


@when("I query a nonexistent endpoint")
def request_nonexistent_endpoint(context):
    context.response = requests.get("http://localhost:8080/nope", timeout=2)


@then("I get a {thing} back")
def assert_thing(context, thing: str):
    assert context.response.status_code == 200
    assert context.response.text == thing


@then("I get error code {status_code:d}")
def assert_error(context, status_code: int):
    assert context.response.status_code == status_code
