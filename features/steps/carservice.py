from behave import given


@given("details about a specific vehicle are available")
def mock_carservice(context):
    context.vin = "OBEYTAILGATER0000"

    context.carservice.post(
        "mappings",
        json={
            "request": {
                "url": f"/vehicles/{context.vin}/details",
                "method": "GET",
                "headers": {
                    "Authorization": {"equalTo": "Bearer im.a.token"},
                },
            },
            "response": {
                "status": 200,
                "headers": {"Content-Type": "application/json"},
                "jsonBody": {
                    "vin": context.vin,
                    "brand": "obey",
                    "model": "tailgater",
                    "color": "black",
                },
            },
        },
    ).raise_for_status()


@given("a specific vehicle does not exist")
def mock_carservice_missing_vehicle(context):
    context.vin = "1234567890ABCDEFG"

    context.carservice.post(
        "mappings",
        json={
            "request": {
                "url": f"/vehicles/{context.vin}/details",
                "method": "GET",
                "headers": {
                    "Authorization": {"equalTo": "Bearer im.a.token"},
                },
            },
            "response": {
                "status": 404,
                "headers": {"Content-Type": "application/json"},
            },
        },
    ).raise_for_status()
