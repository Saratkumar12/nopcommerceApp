import time
import os
from datetime import datetime

import pytest
from selenium import  webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://127.0.0.1/orangehrm-2.5.0.2/login.php")
    driver.find_element(By.NAME, "txtUserName").send_keys("selenium")
    driver.find_element(By.NAME, "txtPassword").send_keys("S@rat1234")
    driver.find_element(By.NAME, "Submit").click()
    driver.implicitly_wait(20)
    yield driver
    time.sleep(5)
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("setup")

        if driver:
            screenshots_dir = "Screenshots"

            if not os.path.exists(screenshots_dir):
                os.makedirs(screenshots_dir)

            file_name = os.path.join(
                screenshots_dir,
                f"{item.name}.png"
            )

            driver.save_screenshot(file_name)
            print(f"\nScreenshot saved: {file_name}")
    @pytest.hookimpl(tryfirst=True)
    def pytest_configure(config):
        today = datetime.now()

