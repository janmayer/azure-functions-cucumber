from behave import then, when


@when("I request a ping")
def request_ping(context):
    context.response = context.application.get("/ping")


@when("I query a nonexistent endpoint")
def request_nonexistent_endpoint(context):
    context.response = context.application.get("/nope")


@then("I get a {thing} back")
def assert_thing(context, thing: str):
    assert context.response.status_code == 200
    assert context.response.text == thing


@then("I get error code {status_code:d}")
def assert_error(context, status_code: int):
    assert context.response.status_code == status_code


@when("the user requests a description for this vehicle")
def request_description(context):
    context.response = context.application.get(f"/vehicles/{context.vin}/description")


@then("the Description Service provides a description for that vehicle")
def ensure_description(context):
    assert context.response.status_code == 200
    assert context.response.json()["vin"] == context.vin
    assert context.response.json()["description"]
