FROM python:3.10-slim

RUN apt update && apt install socat -y

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT socat TCP4-LISTEN:1337,fork,reuseaddr EXEC:/app/main.py