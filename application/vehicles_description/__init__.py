import logging
import os

import azure.functions as func
import openai
import requests
from azure.identity import EnvironmentCredential
from pydantic import BaseModel


class Response(BaseModel):
    vin: str
    description: str


class VehicleDetails(BaseModel):
    vin: str
    brand: str
    model: str
    color: str


def main(req: func.HttpRequest) -> func.HttpResponse:
    vin = req.route_params.get("vin")
    logging.info("vin %s", vin)

    token = EnvironmentCredential().get_token(os.environ["CARSERVICE_SCOPE"]).token
    logging.info("token %s", token)

    vehicle_response = requests.get(
        f"{os.environ['CARSERVICE_BASE_URL']}/vehicles/{vin}/details",
        headers={"Authorization": f"Bearer {token}"},
        timeout=10,
    )
    vehicle_response.raise_for_status()
    vehicle_details = VehicleDetails(**vehicle_response.json())
    logging.info("vehicle details %s", vehicle_details)

    openai.api_key = os.environ["OPENAI_API_KEY"]
    openai_response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Great Prompt for {vehicle_details.json()}.",
        max_tokens=7,
        temperature=0,
    )
    logging.info("vehicle details %s", openai_response)

    description = openai_response["choices"][0]["text"]

    return func.HttpResponse(
        body=Response(vin=vin, description=description).json(indent=4),
        status_code=200,
        mimetype="application/json",
        charset="utf-8",
    )
