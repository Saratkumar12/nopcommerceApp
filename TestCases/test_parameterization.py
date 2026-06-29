import pytest
from selenium.webdriver.common.by import By

#Test Scenarios using Parametrization:
@pytest.mark.parametrize(
    "username,password,expected",
    [
        ("selenium", "S@rat1234", "Pass"),                #valid username and valid password.
        ("selenium", "invalid", "Fail"),                  #username and invalid password
        ("invalid", "S@rat1234", "Fail"),                 #invalid username and valid password.
        ("invaliduserid", "wrongpass", "Fail"),           # invalid username and invalid password.

        ("","S@rat1234","Fail"),                          #Blank Username + Valid Password
        ("selenium"," ","Fail"),                          #Valid Username + Blank Password
        ("","","Fail"),                                   #Blank Username + Blank Password

        ("selenium", "S@rat1234 ","Fail"),         #Username with leading/trailing spaces
        ("selenium", " S@rat1234", "Fail"),                              #Password with leading/trailing spaces
        ("SELENIUM", "S@rat1234", "Fail")                 #Username case sensitivity check




    ]
)

def test_login(setup, username, password, expected):

    setup.find_element(By.NAME, "txtUserName").send_keys(username)
    setup.find_element(By.NAME, "txtPassword").send_keys(password)
    setup.find_element(By.NAME, "Submit").click()

