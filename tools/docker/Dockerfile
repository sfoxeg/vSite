FROM python:3.13.2-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update -y -q && apt install -y -q --no-install-recommends \
    gcc\
    gunicorn \
    sqlite3 \
    postgresql-client-common \
    postgresql-client\
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app/

ADD ../../requirements.txt /app/

RUN pip install --no-cache-dir --upgrade pip
RUN pip install -U --no-cache-dir -r /app/requirements.txt