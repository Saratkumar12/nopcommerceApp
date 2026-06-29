import pytest

@pytest.mark.regression
def test01_regression_1():
    print("run the regression")

@pytest.mark.smoke
def test01_smoke_3():
    print("run the smoke")