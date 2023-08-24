FROM python:3.10-slim

RUN mkdir /CinemaApi

WORKDIR /CinemaApi

COPY requirements.txt .
RUN apt-get update && apt-get install -y git gcc\
    && pip install -r requirements.txt

COPY . .
RUN chmod +x docker/app.sh
