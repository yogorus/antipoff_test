FROM python:3.11-slim

WORKDIR /external_app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install fastapi[all]

COPY . .