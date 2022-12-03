import os
import json
import datetime
import socket

from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def root():
  now = str(datetime.datetime.now())
  hostname = socket.gethostname()
  return(f"Datetime now is {now} from {hostname}")

@app.route("/api/", methods=['GET', 'POST'])
def api():
  x = datetime.datetime.now()
  return jsonify(year=x.year, month=x.month, day=x.day)

@app.route("/status/")
def status():
  return jsonify({ 'status': 'ok' })

if __name__ == "__main__":
  app.run()