FROM python:3.10-alpine

ADD ./app/requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

COPY ./app /app/

EXPOSE 80

WORKDIR /app

CMD [ "flask", "run", "--host=0.0.0.0", "--port=80" ]
