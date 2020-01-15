FROM python:3-alpine

COPY ./uwsgi.ini /uwsgi.ini
COPY ./api /api

WORKDIR /api

RUN apk --no-cache add --update alsa-utils pcre-dev libffi-dev libressl-dev openssh-client\
    && apk --no-cache add --virtual .build-deps \
    gcc make libc-dev linux-headers \
    && pip install uwsgi flask-restful paramiko -i https://mirrors.aliyun.com/pypi/simple \
    && rm -rf .cache/pip \
    && apk del .build-deps

EXPOSE 80

ENTRYPOINT uwsgi --ini /uwsgi.ini
