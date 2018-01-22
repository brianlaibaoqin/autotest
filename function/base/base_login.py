# -*- encoding:utf8 -*-
from time import sleep
from selenium import webdriver

class Login(object):

    # 登录
    def user_login(self,username, password):
        self.driver.find_element_by_class_name("sign ").click()
        iframe = self.driver.find_element_by_id("layui-layer-iframe1")
        self.driver.switch_to_frame(iframe)
        self.driver.find_element_by_id("inputEmail").send_keys(username)
        self.driver.find_element_by_id("inputPassword").send_keys(password)
        self.driver.find_element_by_xpath("//*[@class='inputTxt int4'and @type='submit']").click()
    # 退出
    def user_logout(self):
        self.driver.quit()

    #def checkTXT(self):


    def v_stu_login_suc(self):
        self.driver.find_element_by_xpath("/html/body/header/div/div/ul[2]/li[2]/span").click()
        sleep(2)
        self.driver.find_element_by_link_text("个人中心").click()
        self.driver.find_element_by_link_text("个人信息").click()
        readusername = self.driver.find_element_by_xpath(
            "/html/body/div/div[1]/div/div/div[2]/div[2]/form/input[3]").get_attribute(
            'value')
        if readusername != "":
            return True
        else:
            return False

    def v_stu_login_Fail(self):
        fail_msg = self.driver.find_element_by_xpath("//*[@id='body']/div[2]/div[1]/form/div/ul/li[1]/p").text
        return fail_msg






if __name__ == "__main__":
    aa =Login()
    aa.user_login("bristudent1","12345678")
    sleep(4)
    aa.user_logout()



