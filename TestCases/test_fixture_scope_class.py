import pytest

class TestPerson1:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self):
        print("open the browser setup")
    def test_01(self):
        print("verify the search results")
    def test_02(self):
        print("verify the payment method")

# out put : open the browser-> test01 pass -> test_2 pass so total 3 pass