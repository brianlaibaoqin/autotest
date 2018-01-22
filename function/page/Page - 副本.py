# coding=utf-8
from selenium import webdriver
from  selenium.webdriver.common.by import by
from time import sleep

class Page(object):
    """ 基础类，用于页面对象的的继承"""
    log_url = "http://beta.youngmaker.cn/"
    def __init__(self,selenium_driver,base_url = log_url):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30
    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)
    def _open(self,url):
        url = self.base_url + url
        self.driver.get(url)
        assert self.on_page(),'Did not land on %s' %url
    def open(self):
        self._open(self.url)
    def find_element(self,*loc):
        return self.driver.find_element(*loc)

class Loginpage(Page):
    """登录页面模型"""
    url = "/"

    #定位器
    username_loc = (By.ID,"")
    password_loc = (By.ID,"")
    submit_loc = (By.ID,"")

    #Action
    def type_username(self,username):
        self.find_element(*self.username_loc).send_Keys(username)
    def type_password(self,password):
        self.find_element(*self.password_loc).send_Keys(password)
    def submit(self):
        self.find_element(*self.submit_loc).click()

    def test_user_login(driver,username,password):
        """ 测试获取的用户名/密码是否可以登录"""
        login_page = Loginpage(driver)
        login_page.open()
        login_page.type_username()
        login_page.type_password()
        login_page.submit()

    def main():
        try:
            driver = webdriver.Firefox()
            username = ""
            password = ""
            test_ user_login(driver,username,password):
            sleep(3)
            text = driver.find_element_by_xpath("").text
            assert(text == "")
        finally:
            #关闭浏览器窗口
            driver.quit()
if __name__ == "__main__":
    main()



