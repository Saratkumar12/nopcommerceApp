# test_search_employee.py
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By

def test_admin_companyinfo_generatl(setup):
    actions = ActionChains(setup)

    admin = setup.find_element(By.XPATH, "//span[text()='Admin']")
    company_info = setup.find_element(By.XPATH, "//span[text()='Company Info']")
    general = setup.find_element(By.XPATH, "//span[text()='General']")

    actions.move_to_element(admin) \
        .move_to_element(company_info) \
        .move_to_element(general) \
        .click() \
        .perform()
    setup.implicitly_wait(200)
    setup.find_element(By.XPATH,"//input[@id='editBtn']").click()
