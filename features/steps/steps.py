from behave import then, when


@when("the user requests a description for this vehicle")
def request_description(context):
    context.response = context.application.get(f"/vehicles/{context.vin}/description")


@then("a description for this vehicle is provided")
def ensure_description(context):
    assert context.response.status_code == 200
    assert context.response.json()["vin"] == context.vin
    assert context.response.json()["description"] == "Tolle Karre."


@then("the Description Service returns error code {status_code:d}")
def assert_error(context, status_code: int):
    assert context.response.status_code == status_code
