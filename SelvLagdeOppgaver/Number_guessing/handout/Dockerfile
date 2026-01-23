FROM python:3.10-slim

# Install socat and required packages
RUN apt-get update && \
    apt-get install -y socat gcc && \
    pip install --no-cache-dir pycryptodome && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY chall.py .
COPY entrypoint.sh .

RUN chmod +x entrypoint.sh && ls -l entrypoint.sh

# Expose the port for local TCP access
EXPOSE 1337

ENTRYPOINT ["./entrypoint.sh"]
