import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By




class TestAdminLogin:

    admin_page_url = "https://admin-demo.nopcommerce.com/login"

    username = "admin@yourstore.com"
    password = "admin"
    invalid_username = "invalid"
#test 1
    @allure.severity(allure.severity_level.NORMAL)
    def test_title_verification(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.admin_page_url)
        act_title = self.driver.title
        expt_title = "nopCommerce demo store. Login"
        if act_title == expt_title:
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False
#test2
    @allure.severity(allure.severity_level.CRITICAL)
    def test_valid_admin_login(self):

        self.driver = webdriver.Chrome()
        self.driver.get(self.admin_page_url)

        self.admin_lp = Login_Admin_Page(self.driver)

        self.admin_lp.textbox_username_id(self.username)
        self.admin_lp.textbox_password_id(self.password)
        self.admin_lp.button_admin_login()

        act_dashboard_text = self.driver.find_element(By.XPATH, "//div[@class='content-header']/h1").text
        if act_dashboard_text == "Dashboard":
            assert True
            self.driver.close()
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="validadminlogin",attachment_type=AttachmentType.PNG)
            assert False
#test3
    @allure.severity(allure.severity_level.BLOCKER)
    def test_invalid_admin_login(self):

        self.driver = webdriver.Chrome()
        self.driver.get(self.admin_page_url)

        self.admin_lp = Login_Admin_Page(self.driver)

        self.admin_lp.textbox_username_id(self.invalid_username)
        self.admin_lp.textbox_password_id(self.password)
        self.admin_lp.button_admin_login()

        error_message = self.driver.find_element(By.XPATH, "//span[contains(text(),'Please enter a valid email address.')]").text
        if error_message == "Please enter a valid email address.":

            assert True
            self.driver.close()

        else:
            self.driver.close()
            assert False