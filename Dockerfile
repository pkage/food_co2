FROM ubuntu:latest

RUN mkdir /app
WORKDIR /app

RUN apt-get update
RUN apt-get install build-essential

COPY ./ ./

CMD python3 -m backend.app

EXPOSE 80

