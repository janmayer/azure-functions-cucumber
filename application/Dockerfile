FROM mcr.microsoft.com/azure-functions/python:4-python3.10

ENV AzureFunctionsJobHost__Logging__Console__IsEnabled=true

COPY build/oauth.crt /usr/local/share/ca-certificates/oauth.crt
COPY build/openapi.crt /usr/local/share/ca-certificates/openapi.crt
RUN update-ca-certificates
ENV REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt

COPY application/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
