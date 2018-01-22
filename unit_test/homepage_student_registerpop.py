# coding=utf-8
from time import sleep
from selenium import webdriver
import unittest
import os, sys
from selenium.webdriver.common.keys import Keys
from function.base.html_test_runner import HtmlTestRunner
from selenium.webdriver.common.action_chains import ActionChains
from function.base.DBbase import Deluser
from data.datainfo import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait



class Hp_stu_registerpop(unittest.TestCase):
    """ 点击视频后提示登录测试(弹框学生账号注册)"""

    def setUp(self):
        fp = webdriver.FirefoxProfile(path)
        self.driver = webdriver.Firefox(fp)
        self.driver.implicitly_wait(30)
        self.driver.get(url)
        aaaa = Deluser()
        aaaa.delusername()




    def test_01(self):
        aa = self.driver.find_element_by_xpath("//li[@class='li2']/p[1]")
        self.driver.execute_script("arguments[0].scrollIntoView(false);", aa)
        sleep(5)
        self.driver.find_element_by_xpath("//li[@class='li2']/p[1]").click()
        sleep(5)

    def test_02(self):
        aa = self.driver.find_element_by_xpath("//li[@class='li4']/p[1]")
        self.driver.execute_script("arguments[0].scrollIntoView(false);", aa)
        sleep(5)
        self.driver.find_element_by_xpath("//li[@class='li4']/p[1]").click()
        sleep(5)

    def test_03(self):
        aa = self.driver.find_element_by_xpath("//li[@class='li5']/p[1]")
        self.driver.execute_script("arguments[0].scrollIntoView(false);", aa)
        sleep(5)
        self.driver.find_element_by_xpath("//li[@class='li5']/p[1]").click()
        sleep(5)

    def test_04(self):
        aa = self.driver.find_element_by_xpath("//li[@class='li6']/p[1]")
        self.driver.execute_script("arguments[0].scrollIntoView(false);", aa)
        sleep(5)
        self.driver.find_element_by_xpath("//li[@class='li6']/p[1]").click()
        sleep(5)

    def tearDown(self):
        #显示等待
        element = WebDriverWait(self.driver,15).until(lambda x: x.find_element_by_xpath("//*[@id='register_b']"))
        sleep(2)
        element.click()
        sleep(1)
        aa = self.driver.find_element_by_xpath("//div[@class='layui-layer-content']/iframe")
        self.driver.switch_to_frame(aa)
        self.driver.find_element_by_xpath("//*[@id = 'inputEmail']").send_keys(username)
        self.driver.find_element_by_xpath("//*[@id='inputPassword1']").send_keys(password)
        self.driver.find_element_by_xpath("//*[@id='check1']").send_keys(password)
        self.driver.find_element_by_xpath("//*[@id='inputPassword2']").send_keys(verifynum)
        self.driver.find_element_by_xpath("//input[@placeholder='请输入电子邮箱'and @nullmsg='请填写邮箱']").send_keys(mailnum)
        self.driver.find_element_by_xpath("//*[@id='teachernub']/input").send_keys(teachername)
        self.driver.find_element_by_xpath("//button[@class='inputTxt int4' and @type='submit']").click()
        # 验证学生注册
        self.driver.switch_to_default_content()
        self.driver.find_element_by_xpath("/html/body/header/div/div/ul[2]/li[2]/span").click()
        sleep(2)
        self.driver.find_element_by_link_text("个人中心").click()
        self.driver.find_element_by_link_text("个人信息").click()
        readname = self.driver.find_element_by_xpath("//input[@id='username' and @class='int']").get_attribute("value")
        self.assertEqual(readname, username, msg="学生账号注册fail")
        print(readname,"学生账号注册PASS")
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()



