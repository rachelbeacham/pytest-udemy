from pytest import mark

@mark.television
class TelevisionTests:
  @mark.skip
  @mark.parametrize('tv_brand', [
      ('Samsung'),
      ('Sony'),
      ('Vizio'),
    ]
  )
  # one way to use parameters
  # built into the test using special mark keyword, parametrize
  def test_television_turns_on(self, tv_brand):
    print(f"{tv_brand} turns on as expected")

  # another way to use parameters - using tv_brand fixture (in conftest.py)
  # Makes it easier to reuse same parameters and make edits to params (only need to edit the fixture)
  @mark.skip
  def test_television_with_fixture(self, tv_brand):
    print(f"{tv_brand} works as expected")

  # Another way to use parmeters - using json data
  # json file is connected in conftest.py
  def test_television_with_json_data(self, tv_brand_data):
    print(f"{tv_brand_data} works as expected")
