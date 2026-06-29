from selenium.webdriver.common.by import By
from test_mobile_randomdata.randomdata import RandomData

from TestCases.Basic_Selenium.test_webElements import driver

mobile = RandomData.generate_mobile()

driver.find_element(By.ID, "phone").send_keys(mobile)

