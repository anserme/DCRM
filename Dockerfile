FROM python:3.7

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN apk add --update mysql mysql-client && rm -f /var/cache/apk/*
COPY . .
CMD ["./uwsgi-run.sh"]

