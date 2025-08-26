FROM --platform=$BUILDPLATFORM python:3.10-alpine AS builder
WORKDIR /app
COPY app /app
#RUN mkdir -p /app/api
#COPY /api /app/api
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["app.py"]
