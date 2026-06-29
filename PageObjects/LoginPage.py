from selenium.webdriver.common.by import By


class Login_Admin_Page:

    textbox_username = "Email"
    textbox_password = "Password"
    button_login = "//button[@type='submit']"

    def __init__(self, driver):
        self.driver = driver

    def textbox_username_id(self, username):
        self.driver.find_element(By.ID, self.textbox_username).clear()
        self.driver.find_element(By.ID, self.textbox_username).send_keys(username)

    def textbox_password_id(self, password):
        self.driver.find_element(By.ID, self.textbox_password).clear()
        self.driver.find_element(By.ID, self.textbox_password).send_keys(password)

    def button_admin_login(self):
        self.driver.find_element(By.XPATH, self.button_login).click()