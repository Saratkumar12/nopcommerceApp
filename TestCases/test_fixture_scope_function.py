import pytest
class TestEmp:

    @pytest.fixture(scope="function")
    def setup(self):
        print("Browser Open")

    def test_login(self, setup):
        print("Login")

    def test_logout(self, setup):
        print("Logout")

 # login ki browser set up open avuthundi and logout ki kuda browser open avuthudi
 #for HTML Reports:  pytest -v -s TestCases/test_fixture_autouse.py --html=Reports/report.html