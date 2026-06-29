import pytest

class TestPerson:
    @pytest.fixture(autouse=True)
    def setup(self):
        print("open the browser setup")
    def test_01(self):
        print("login with user id ")
    def test_02(self):
        print("login admin page with password")

# when you give scope = true anty it automatic every method ki run avuthidi