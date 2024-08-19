from pytest import mark
import time

# Lesson:
# Can install a pytest extension that allows you to run multiple tests at once, therefor saving time.
# the 4 test below have a delay of 5 seconds each (simulating a test that takes longer to run)
# a regular run of all chemistry tests took 20.04 seconds
# test run command: pytest -m chemistry -s -v (-m chemistry specifies the chemistry marker)  (-s allows the print statement to run) (-v means verbose which is just more detailed info)
# run    pip install pytest-xdist   within your virtual environment
# Now you can run the tests with a slightly different command
# pytest -m chemistry -s -v -n4 (-n4 represents the Nummber of threads to use = 4)
# Now each tests runs on a different thread, each taking 5 seconds due to the delay we added
# The total time for the 4 tests to run is now ~5.60 seconds rather than ~20 seconds
# If you don't know how many threads you want to add to the command, can mess around to see what works best or use -nauto and the extension will determine the amount of threads for you
@mark.chemistry
class ChemistryTests:
  def test_result_1_completes_as_expected(self):
    time.sleep(5)
    print ("Result 1 has completed")

  def test_result_2_completes_as_expected(self):
    time.sleep(5)
    print ("Result 2 has completed")

  def test_result_3_completes_as_expected(self):
    time.sleep(5)
    print ("Result 3 has completed")

  def test_result_4_completes_as_expected(self):
    time.sleep(5)
    print ("Result 4 has completed")
