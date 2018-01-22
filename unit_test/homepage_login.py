# coding=utf-8
from time import sleep
from selenium import webdriver
import unittest
import os ,sys
import time
from selenium.webdriver.common.keys import Keys
from function.base.html_test_runner import HtmlTestRunner
import pymysql
from selenium.webdriver.common.action_chains import ActionChains
from function.base.mySQLDB import DB
from data.datainfo import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
class Hp_login (unittest.TestCase):
      """ 点击视频后提示登录测试(弹框)"""
      def setUp(self):
        fp = webdriver.FirefoxProfile(path)
        self.driver = webdriver.Firefox(fp)
        self.driver.implicitly_wait(30)
        self.driver.get(url)

      def tearDown(self):
        try:
            self.driver.find_element_by_xpath("//li[@class='name']/span").click()
            sleep(2)
            aa = self.driver.find_element_by_xpath("//li[@class='name']/span").text
            print(aa)
            self.assertEqual(aa,username)
        except Exception as msg:
            print(msg)
            self.driver.get_screenshot_as_file("D:\\youngmaker_auto\\report\\" + time.strftime("%Y-%m-%d %H_%M_%S") + "homepage_login_msg.jpg")

        self.driver.quit()

      def test_01(self):
        aa = self.driver.find_element_by_xpath("//li[@class='li2']/p[1]")
        self.driver.execute_script("arguments[0].scrollIntoView(false);", aa)
        self.driver.find_element_by_xpath("//li[@class='li2']/p[1]").click()
        sleep(8)

        self.driver.find_element_by_xpath("//*[@id='inputEmail']").clear()
        self.driver.find_element_by_xpath("//*[@id='inputEmail']").send_keys(username)
        sleep(2)
        self.driver.find_element_by_xpath("//*[ @ id = 'inputPassword']").clear()
        self.driver.find_element_by_xpath("//*[ @ id = 'inputPassword']").send_keys(password)
        self.driver.find_element_by_xpath("//*[@class='sureBtn' and @type='submit']").click()
      def test_02(self):
        aa = self.driver.find_element_by_xpath("//li[@class='li4']/p[1]")
        self.driver.execute_script("arguments[0].scrollIntoView(false);", aa)
        self.driver.find_element_by_xpath("//li[@class='li4']/p[1]").click()
        sleep(8)
        self.driver.find_element_by_xpath("//*[@id='inputEmail']").clear()
        self.driver.find_element_by_xpath("//*[@id='inputEmail']").send_keys(username)
        sleep(2)
        self.driver.find_element_by_xpath("//*[ @ id = 'inputPassword']").clear()
        self.driver.find_element_by_xpath("//*[ @ id = 'inputPassword']").send_keys(password)
        self.driver.find_element_by_xpath("//*[@class='sureBtn' and @type='submit']").click()

      def test_03(self):

        aa = self.driver.find_element_by_xpath("//li[@class='li5']/p[1]")
        self.driver.execute_script("arguments[0].scrollIntoView(false);",aa)
        self.driver.find_element_by_xpath("//li[@class='li5']/p[1]").click()
        wait = WebDriverWait(self.driver,15)
        wait.until(EC.element_to_be_clickable((By.ID,'inputEmail'))).click()
        self.driver.find_element_by_xpath("//*[@id='inputEmail']").clear()
        self.driver.find_element_by_xpath("//*[@id='inputEmail']").send_keys(username)
        sleep(1)
        self.driver.find_element_by_xpath("//*[ @ id = 'inputPassword']").clear()
        self.driver.find_element_by_xpath("//*[ @ id = 'inputPassword']").send_keys(password)
        self.driver.find_element_by_xpath("//*[@class='sureBtn' and @type='submit']").click()

      def test_04(self):
        aa = self.driver.find_element_by_xpath("//li[@class='li6']/p[1]")
        self.driver.execute_script("arguments[0].scrollIntoView(false);", aa)
        self.driver.find_element_by_xpath("//li[@class='li6']/p[1]").click()
        sleep(8)
        self.driver.find_element_by_xpath("//*[@id='inputEmail']").clear()
        self.driver.find_element_by_xpath("//*[@id='inputEmail']").send_keys(username)
        sleep(2)
        self.driver.find_element_by_xpath("//*[ @ id = 'inputPassword']").clear()
        self.driver.find_element_by_xpath("//*[ @ id = 'inputPassword']").send_keys(password)
        self.driver.find_element_by_xpath("//*[@class='sureBtn' and @type='submit']").click()

if __name__ == "__main__":
    unittest.main()









