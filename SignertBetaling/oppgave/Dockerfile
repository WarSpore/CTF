FROM python:3.8.20-slim-bookworm

WORKDIR /app

COPY krav.txt /app
RUN pip3 install -r krav.txt
RUN echo "deb http://deb.debian.org/debian/ testing main" > /etc/apt/sources.list
RUN apt-get update && apt-get install -y libc6 libc-bin

COPY *.py /app
COPY templates /app/templates
COPY python /usr/local/bin/python3.8

RUN adduser --disabled-password --gecos '' webapp
USER webapp

CMD ["python3", "app.py"]