FROM mcr.microsoft.com/azure-functions/python:4-python3.10

ENV AzureFunctionsJobHost__Logging__Console__IsEnabled=true

RUN mkdir /etc/secrets/
ENV FUNCTIONS_SECRETS_PATH=/etc/secrets
ENV AzureWebJobsSecretStorageType=Files
ADD development/host.json /etc/secrets/host.json

COPY application/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
