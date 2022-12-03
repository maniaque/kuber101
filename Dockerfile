FROM alpine

RUN apk add --no-cache python3 uwsgi uwsgi-python3 py3-pip

ADD ./app/requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

COPY ./app /app/

EXPOSE 80

WORKDIR /app

CMD [ "uwsgi", "--plugin=python3", "--socket=0.0.0.0:80", "--protocol=http", "--mount=/=app.py", "--callable=app" ]
