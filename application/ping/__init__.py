import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    """ doctest
    >>> req = func.HttpRequest(method="get", url="ping", body=None)
    >>> res = main(req)
    >>> res.get_body().decode("utf-8")
    'pong'
    """
    logging.info("Python HTTP trigger function processed a request: %s", req.url)
    return func.HttpResponse("pong")
