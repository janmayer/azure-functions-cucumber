import httpx


def before_all(context):
    context.application = httpx.Client(base_url="http://localhost:8080")
    context.carservice = httpx.Client(base_url="http://localhost:9000/__admin")
    context.openai = httpx.Client(
        base_url="https://localhost:9002/__admin", verify=False
    )


def before_scenario(context, _):
    for mock in [context.carservice, context.openai]:
        mock.delete("mappings").raise_for_status()
        mock.delete("requests").raise_for_status()
