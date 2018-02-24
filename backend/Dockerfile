FROM python:alpine3.6
WORKDIR /usr/src/app

RUN apk update \
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN apk del build-deps

COPY . .
CMD [ "gunicorn", "-b","0.0.0.0:8000","app.main:app" ]