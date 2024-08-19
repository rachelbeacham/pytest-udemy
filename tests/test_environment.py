from pytest import mark

@mark.xfail(reason="Env is not QA")
# special pytest mark keyword, xfail
# shows the tests as XFAIL (expected failure), can add optional reason to let others know why
@mark.config
def test_environment_is_qa(app_config):
  base_url = app_config.base_url
  port = app_config.app_port

  assert base_url == 'https://myqa-env.com'
  assert port == 80

@mark.config
def test_environment_is_dev(app_config):
  base_url = app_config.base_url
  port = app_config.app_port

  assert base_url == 'https://mydev-env.com'
  assert port == 8080

@mark.skip(reason="staging is not a real env")
# special pytest mark keyword, skip
# shows the tests as SKIPPED, can add optional reason to let others know why
# better than commenting the test out, as you may forget it exists
@mark.config
def test_environment_is_staging(app_config):
  base_url = app_config.base_url
  assert base_url == 'staging'
