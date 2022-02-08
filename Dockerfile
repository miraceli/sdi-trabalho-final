FROM python:3.7-alpine

ADD ./aplication /aplication
ADD requirements.txt /aplication/

WORKDIR /aplication

RUN sh -c "python3 -m pip install -r /aplication/requirements.txt"