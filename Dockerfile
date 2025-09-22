FROM python:3.13.2-slim-bullseye

RUN apt update -y -q && apt install -y -q --no-install-recommends \
    gunicorn \
    sqlite3 \
    postgresql-client-common \
    postgresql-client\
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN addgroup -S app && adduser --disabled-password --no-create-home app
WORKDIR /app/
RUN mkdir /app/staticfiles/ && mkdir /app/mediafiles
RUN chown -R app:app /app && chown -R app:app /app/staticfiles && chown -R app:app /app/staticfiles

ADD requirements.txt /app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --no-cache-dir --upgrade pip
RUN pip install -U --no-cache-dir -r /app/requirements.txt

USER app