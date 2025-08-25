FROM --platform=$BUILDPLATFORM python:3.10-alpine AS builder
#FROM python:3.9-slim-buster
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["app.py"]
