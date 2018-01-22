# coding=utf-8
from time import sleep
from selenium import webdriver
from data.datainfo import *
from function.base.DBbase import Deluser
import os
import unittest


class Flashpage_reg_login(unittest.TestCase):
    """ flashpage 登录注册测试"""
    def setUp(self):
        fp = webdriver.FirefoxProfile(path)
        fp.set_preference("plugin.state.flash", 2)
        self.driver = webdriver.Firefox(fp)
        self.driver.implicitly_wait(30)
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.find_element_by_link_text(u"编程").click()
        sleep(30)


    def tearDown(self):
        self.driver.quit()



    def test_1_sturegister(self):
        """ flashpage 学生账号注册"""
        xusername = Deluser()
        xusername.delusername()
        os.system("D:\\youngmaker_auto\\function\AU3\\stu_register.exe")
        print("stu_register done 01")

    def test_2_login(self):
        """ flashpage学生账号登录"""
        os.system("D:\\youngmaker_auto\\function\AU3\\login.exe")
        self.driver.refresh()
        sleep(2)
        all_handles = self.driver.window_handles
        Cur = self.driver.current_window_handle
        self.driver.switch_to_window(all_handles[2])
        try:
            flash_username = self.driver.find_element_by_xpath("//*[@id='head']/ul[2]/li[2]/span").text
            self.assertNotEqual(flash_username,"")
            print(flash_username, "stu_登录成功")
        except:
            print("测试出错了")

    def test_3_tearegister(self):
        """ flashpage 老师账号注册"""
        xusername = Deluser()
        xusername.delusername()
        os.system("D:\\youngmaker_auto\\function\AU3\\tea_register.exe")
        print("tea_register done 03")

    def test_4_tealogin(self):
        os.system("D:\\youngmaker_auto\\function\AU3\\login.exe")
        self.driver.refresh()
        sleep(2)
        all_handles2 = self.driver.window_handles
        self.driver.switch_to_window(all_handles2[2])
        try:
            flash_username = self.driver.find_element_by_xpath("//*[@id='head']/ul[2]/li[2]/span").text
            self.assertNotEqual(flash_username, "")

        except:
            print("测试出错了")


if __name__ == "__main__":
    unittest.main()


