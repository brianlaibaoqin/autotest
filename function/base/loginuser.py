# coding=utf-8
from selenium import webdriver
from function.base.base_login import Login
from time import sleep
class LoginTest(object):
    def __init__(self):
        fp = webdriver.FirefoxProfile("D:\\youngmaker_auto\\function\\firefoxPro")
        self.driver = webdriver.Firefox(fp)
        self.driver.implicitly_wait(10)
        self.driver.get(url)
    def test_login(self):
        Login().user_login(self.driver)

    def test_logout(self):
        Login().log_out(self.driver)


if __name__ == "__main__":
    aa = LoginTest()
    aa.test_login()
    sleep(3)
    aa.test_logout()



