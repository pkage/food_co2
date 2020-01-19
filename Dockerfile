FROM ubuntu:latest

USER root

RUN mkdir /app
WORKDIR /app

RUN apt-get update
# RUN apt-get install build-essential -y

COPY ./backend ./backend

RUN apt-get install python3-pip -y
RUN pip3 install pip
RUN pip3 install -r requirements.txt

CMD ["python3", "-m", "backend.app"]

EXPOSE 80

