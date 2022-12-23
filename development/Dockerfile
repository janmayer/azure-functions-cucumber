FROM python:3.9

COPY application/requirements.txt application-requirements.txt
COPY development/requirements.txt development-requirements.txt
RUN pip install --no-cache-dir -r application-requirements.txt -r development-requirements.txt
