import requests


def before_all(context):
    requests.post(
        "http://localhost:8080/admin/host/restart",
        headers={"x-functions-key": "MY_MASTER_KEY"},
        timeout=10,
    ).raise_for_status()
