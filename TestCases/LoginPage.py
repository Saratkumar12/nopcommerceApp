import threading
import time

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common import alert
from selenium.webdriver.common.by import By
import pytest

import threading
import time

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common import alert
from selenium.webdriver.common.by import By
class TestHRM:
        @pytest.mark.skip(reason = "knownbug")
        @allure.severity(allure.severity_level.NORMAL)
        @pytest.mark.order(2)
        def test_01_Titlepage(self,setup):
            print(setup.title)

        @pytest.mark.skip(reason="knownbug")
        @allure.severity(allure.severity_level.MINOR)
        @pytest.mark.order(3)
        def test_2_logo(self, setup):
         logo = setup.find_element(By.XPATH, "//img")
         assert logo.is_displayed(), "Logo is not displayed"
#Enter a valid registered email and the correct password click Login
        @pytest.mark.skip(reason="knownbug")
        @allure.severity(allure.severity_level.CRITICAL)
        @pytest.mark.order(5)
        def test_3_login(self,setup):

            setup.find_element(By.NAME, "txtUserName").send_keys("selenium")
            setup.find_element(By.NAME, "txtPassword").send_keys("S@rat1234")
            setup.find_element(By.NAME, "Submit").click()

#Enter an unregistered or improperly formatted email and a valid password click Login
        @pytest.mark.skip(reason="knownbug")
        @allure.severity(allure.severity_level.BLOCKER)
        @pytest.mark.order(4)
        def test_4_invalid_email_pass(self,setup):
            setup.find_element(By.NAME,"txtUserName").send_keys("Seleniums")
            setup.find_element(By.NAME,"txtPassword").send_keys("S@ratkumar")
            setup.find_element(By.NAME,"Submit").click()

#Leave both Email and Password fields completely blank and click Login
        @pytest.mark.skip(reason="knownbug")
        @pytest.mark.order(1)
        def test_05_leave_use_pass(self,setup):
            setup.find_element(By.NAME,"Submit").click()
            alert = setup.switch_to.alert
            alert.accept()
#Parameterization
        #single Login testcase with multiple test data

