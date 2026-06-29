import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def setup():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demoapps.qspiders.com/ui/radio?sublist=0")

    yield driver

    driver.quit()


def test_title(setup):

    driver = setup

    print(driver.title)