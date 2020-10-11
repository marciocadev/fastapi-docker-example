######### BASE #########
FROM python:3.8-slim AS base

WORKDIR /fast

COPY ./requirements.txt /fast/requirements.txt

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

RUN pip install -r requirements.txt \
    && apt-get remove gcc -y \
    && rm -rf /root/.cache/pip

RUN apt-get autoremove -y \
    && apt-get autoclean

COPY . /fast/

######### DEBUG #########
FROM base AS debug

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG True

COPY ./requirements-dev.txt /fast/requirements.txt

RUN pip install -r requirements.txt

CMD python run.py

######### PRODUCTION #########
FROM base AS prod

# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
RUN adduser --disabled-password appuser \
    && chown -R appuser /fast/app
    
USER appuser

ENV DEBUG False

CMD uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
