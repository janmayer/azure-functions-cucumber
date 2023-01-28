FROM mcr.microsoft.com/azure-functions/python:4-python3.10

ENV AzureFunctionsJobHost__Logging__Console__IsEnabled=true

COPY application/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY application /home/site/wwwroot
