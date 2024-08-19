from pytest import mark
import requests

@mark.api
def test_twitter_is_present():
  resp = requests.get("http://techstepacademy.com/training-ground")
  assert "twitter" in resp.text
