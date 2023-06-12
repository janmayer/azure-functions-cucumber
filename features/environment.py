import httpx


def before_all(context):
    context.application = httpx.Client(base_url="http://localhost:8080")
    context.carservice = httpx.Client(base_url="http://localhost:9000/__admin")

    context.application.post(
        "/admin/host/restart",
        headers={"x-functions-key": "MY_MASTER_KEY"},
        timeout=10,
    ).raise_for_status()


def before_scenario(context, _):
    context.carservice.delete("mappings").raise_for_status()
    context.carservice.delete("requests").raise_for_status()
