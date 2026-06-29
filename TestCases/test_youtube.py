import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from Base_Page.Admin_Login import Login_Admin_Page


class test_01_admin_login:
    admin_page_url = "https://admin-demo.nopcommerce.com/login"

    username = "admin@yourstore.com"
    passowrd = "admin"
    invalid_username = "invalid"


def test_title_verification(self):
    self.driver = webdriver.Chrome()
    self.driver.get(self.admin_page_url)
    act_title = self.driver.title
    expt_title = "Your Store. Login"
    if act_title == expt_title:
        assert True
        self.driver.close()
    else:
        self.driver.close()
        assert False


def test_valid_admin_login(self):
    self.driver = webdriver.Chrome()
    self.driver.get(self.admin_page_url)
    self.admin_lp = Login_Admin_Page()
    self.admin_lp.textbox_username_id(self.username)
    self.admin_lp.textbox_password_id(self.password)
    self.admin_lp.button_admin_login()
    act_dashboard_text = self.driver.find_element(By.XPATH, "//div@class='content-header']/h1").text
    if act_dashboard_text == "Dashboard":
        assert True
        self.driver.close()
    else:
        self.driver.close()
        assert False


def test_invalid_admin_login(self):
    self.driver = webdriver.Chrome()
    self.driver.get(self.admin_page_url)
    self.admin_lp = Login_Admin_Page()
    self.admin_lp.textbox_username_id(self.invalid_username)
    self.admin_lp.textbox_password_id(self.password)
    self.admin_lp.button_admin_login()
    error_message = self.driver.find_element(By.XPATH, "//li.").text
    if error_message == "No customer account found":
        assert True
        self.driver.close()

    else:
        self.driver.close()
        assert False



