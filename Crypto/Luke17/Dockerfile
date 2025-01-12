FROM python:3.12-slim-bookworm

RUN useradd -d /home/ctf -m -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd

WORKDIR /home/ctf

COPY requirements.txt /home/ctf/
RUN pip install -r requirements.txt

COPY ynetd run.sh /home/ctf/
COPY *.py flag*.txt /home/ctf/

RUN chown -R root:root /home/ctf
RUN chmod -R a+rx /home/ctf
USER ctf

CMD ./ynetd -p 1024 /home/ctf/run.sh