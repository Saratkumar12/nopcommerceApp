from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://demoapps.qspiders.com/ui/dropdown?sublist=0")
driver.maximize_window()

# deliver details :

#element = WebDriverWait(driver,10).until(EC.((By.ID,"")))

element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "country_code"))
)

code = Select(element)

code.select_by_index(3)

driver.find_element(By.NAME,"ph").send_keys("9988776655")


import random

def generate_phone():
    return str(random.randint(6000000000, 9999999999))

print(generate_phone())

