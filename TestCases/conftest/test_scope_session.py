import pytest
@pytest.fixture(scope='session',autouse=True)
def myfixture():
    print("my fixture is calling")

