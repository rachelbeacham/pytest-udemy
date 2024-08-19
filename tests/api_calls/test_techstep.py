from pytest import mark
import requests

@mark.api
def test_get_successful_response():
  resp = requests.get('http://techstepacademy.com/training-ground')
  assert resp.status_code == 200
