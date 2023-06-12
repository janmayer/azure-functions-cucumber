from behave import given


@given("details about a specific vehicle are available")
def mock_carservice(context):
    context.vin = "OBEYTAILGATER0000"

    context.carservice.post(
        "mappings",
        json={
            "request": {
                "url": "/vehicles/OBEYTAILGATER0000/details",
                "method": "GET",
                "headers": {
                    "Authorization": {"equalTo": "Bearer im.a.token"},
                },
            },
            "response": {
                "status": 200,
                "headers": {"Content-Type": "application/json"},
                "jsonBody": {
                    "vin": "OBEYTAILGATER0000",
                    "brand": "obey",
                    "model": "tailgater",
                    "color": "black",
                },
            },
        },
    ).raise_for_status()
