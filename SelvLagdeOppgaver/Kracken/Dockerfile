FROM python:3.11-slim

# System deps + socat (for remote interactive PTY over TCP)
RUN apt-get update && apt-get install -y \
    gcc \
    gdb \
    libc6-dev \
    libffi-dev \
    socat \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip install --no-cache-dir \
    pycryptodome \
    pwntools

COPY chall.py .

# Expose a TCP port for remote connections
EXPOSE 4444

# One PTY per connection, runs your script as-is
CMD ["socat", "-T", "300", "TCP-LISTEN:4444,reuseaddr,fork", "EXEC:python3 /app/chall.py,pty,stderr,setsid,sane"]
