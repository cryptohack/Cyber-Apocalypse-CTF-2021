FROM ubuntu:20.04

RUN apt update && apt -y dist-upgrade && apt -y install xinetd python3 python3-pip && python3 -m pip install pycryptodome

RUN useradd ctf

RUN mkdir /app && chown ctf /app
WORKDIR /app

COPY flag.txt /app/flag.txt
COPY forge_of_empires.py /app/forge_of_empires.py
COPY forge_of_empires.xinetd /etc/xinetd.d/forge_of_empires

RUN chown -R ctf /app

CMD xinetd -dontfork
EXPOSE 5000
