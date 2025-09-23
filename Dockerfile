FROM python:3.13.2-slim-bullseye

RUN apt update -y -q && apt install -y -q --no-install-recommends \
    gunicorn \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app/

ADD requirements.txt /app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --no-cache-dir --upgrade pip
RUN pip install -U --no-cache-dir -r /app/requirements.txt