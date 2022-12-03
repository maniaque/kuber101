import os
import sys
import pytest
import json

import app

@pytest.fixture
def client():
  return app.app.test_client()

def test_root(client):
  response = client.get("/")
  assert b'Datetime now is' in response.data

def check_api(obj):
  assert obj['year']
  assert obj['month']
  assert obj['day']

def test_api_get(client):
  response = client.get("/api/")
  data = json.loads(response.data)
  check_api(data)

def test_api_post(client):
  response = client.post("/api/")
  data = json.loads(response.data)
  check_api(data)