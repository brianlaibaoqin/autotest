# coding=utf-8
from time import sleep
from selenium import webdriver
import unittest
import os, sys
import time
from selenium.webdriver.common.keys import Keys
from function.base.html_test_runner import HtmlTestRunner
import pymysql
from selenium.webdriver.common.action_chains import ActionChains
from function.base.DBbase import Deluser
from data.datainfo import *
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait


class Hp_tea_registerpop(unittest.TestCase):
    """ 点击视频后提示登录测试(弹框老师账号注册)"""

    def setUp(self):
        fp = webdriver.FirefoxProfile(path)
        self.driver = webdriver.Firefox(fp)
        self.driver.implicitly_wait(30)
        self.driver.get(url)
        xusername = Deluser()
        xusername.delusername()



    def test_01(self):
        aa = self.driver.find_element_by_xpath("//li[@class='li2']/p[1]")
        self.driver.execute_script("arguments[0].scrollIntoView(false);", aa)

        self.driver.find_element_by_xpath("//li[@class='li2']/p[1]").click()
        sleep(5)

    def test_02(self):
        aa = self.driver.find_element_by_xpath("//li[@class='li4']/p[1]")
        self.driver.execute_script("arguments[0].scrollIntoView(false);", aa)

        self.driver.find_element_by_xpath("//li[@class='li4']/p[1]").click()
        sleep(5)

    def test_03(self):
        aa = self.driver.find_element_by_xpath("//li[@class='li5']/p[1]")
        self.driver.execute_script("arguments[0].scrollIntoView(false);", aa)

        self.driver.find_element_by_xpath("//li[@class='li5']/p[1]").click()
        sleep(5)

    def test_04(self):
        aa = self.driver.find_element_by_xpath("//li[@class='li6']/p[1]")
        self.driver.execute_script("arguments[0].scrollIntoView(false);", aa)

        self.driver.find_element_by_xpath("//li[@class='li6']/p[1]").click()
        sleep(1)

    def tearDown(self):
        element = WebDriverWait(self.driver,15).until(lambda x: x.find_element_by_xpath("//*[@id='register_b']"))
        sleep(2)
        element.click()
        sleep(1)
        bb = self.driver.find_element_by_xpath("//div[@class='layui-layer-content']/iframe")
        self.driver.switch_to_frame(bb)
        sleep(2) # 必须暂停一下，出过意外了。
        self.driver.find_element_by_xpath("//input[ @ id = 'teacher']").click()
        self.driver.find_element_by_xpath("// *[@id = 'inputEmail']").send_keys(username)
        self.driver.find_element_by_xpath("//*[@id='inputPassword1']").send_keys(password)
        self.driver.find_element_by_xpath("//*[@id='check1']").send_keys(password)
        self.driver.find_element_by_xpath("//*[@id='inputPassword2']").send_keys(verifynum)
        self.driver.find_element_by_xpath("//input[@placeholder='请输入电子邮箱'and @nullmsg='请填写邮箱']").send_keys(mailnum)
        sleep(3)
        self.driver.find_element_by_xpath("//button[@class='inputTxt int4' and @type='submit']").click()
        sleep(3)
        # 重新切换回内嵌iframe
        self.driver.switch_to.default_content()
        cc = self.driver.find_element_by_xpath("//div[@class='layui-layer-content']/iframe")
        self.driver.switch_to_frame(cc)

        self.driver.find_element_by_xpath("//input[@placeholder='请输入用户名'and @id='name']").send_keys(realchinesename)
        self.driver.find_element_by_xpath("//input[@id = 'wumen']").click()
        self.driver.find_element_by_xpath("//select[ @ id = 'search_area_0']").click()   # 选择第1个学校区域框
        self.driver.find_element_by_xpath("//select[ @ id = 'search_area_0']/option[10]").click()
        self.driver.find_element_by_xpath("//select[ @ id = 'search_area_2']").click()      # 选择第2个学校区域框
        self.driver.find_element_by_xpath("//select[ @ id = 'search_area_2']/option[12]").click()
        self.driver.find_element_by_xpath("//select[ @ id = 'search_area_3']").click()      # 选择第3个学校区域框
        cc = self.driver.find_element_by_xpath("//select[ @ id = 'search_area_3']/option[5]")
        ActionChains(self.driver).double_click(cc).perform()
        self.driver.find_element_by_xpath("//input[@placeholder='请输入学校名称']").send_keys(shoolname)
        self.driver.find_element_by_xpath("//input[@placeholder='请输入个人手机号']").send_keys(mpnum)
        self.driver.find_element_by_xpath("//input[@placeholder='请输入QQ号']").send_keys(QQnum)
        self.driver.find_element_by_xpath("//div[@class='inputTxt int4']").click()

        # 验证老师注册
        self.driver.switch_to_default_content()
        ff = self.driver.find_element_by_xpath("//*[@id='RightPot']/li[2]/span")
        ActionChains(self.driver).move_to_element(ff).perform()
        sleep(2)
        gg = self.driver.find_element_by_link_text("个人中心")
        gg.click()
        self.driver.find_element_by_link_text("个人信息").click()
        readname = self.driver.find_element_by_xpath("//input[@id='username' and @class='int']").get_attribute("value")
        self.assertEqual(readname, username, msg="老师账号注册fail")
        print(readname,"老师账号注册PASS")
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()



