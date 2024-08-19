from pytest import fixture
from config import Config
import json

data_path = 'test_data.json'

def pytest_addoption(parser):
  parser.addoption("--env", action="store", help="Environment to run tests against")


@fixture(scope='session')
def env(request):
  return request.config.getoption("--env")

@fixture(scope='session')
def app_config(env):
  cfg = Config(env)
  return cfg

@fixture(params=['samsung', 'sony', 'vizio'])
def tv_brand(request):
  brand = request.param
  return brand

def load_test_data(path):
  with open(path) as data_file:
    data = json.load(data_file)
    return data

@fixture(params=load_test_data(data_path))
def tv_brand_data(request):
  data = request.param
  return data
