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
from function.base.DBbase import Deluser
from data.datainfo import *

class login(unittest.TestCase):
    """网站登录注册测试"""
    def setUp(self):               # 打开登录页面
         fp = webdriver.FirefoxProfile(path)
         self.br = webdriver.Firefox(fp)
         self.br.implicitly_wait(30)
         self.br.get(url)
    def tearDown(self):
         self.br.quit()
         pass
    #注册学生账号
    def test_01_student_register(self):
        xusername = Deluser()
        xusername.delusername()

        self.br.find_element_by_class_name("register").click()  # 点击注册按钮
        self.br.find_element_by_id("layui-layer-iframe1").click()  # 选取表单iframe1
        self.br.switch_to.default_content()
        self.br.switch_to_frame("layui-layer-iframe1")
        self.br.find_element_by_name("username").send_keys(username)
        self.br.find_element_by_name("password").send_keys(password)
        self.br.find_element_by_name("repassword").send_keys(password)
        self.br.find_element_by_name("verify").send_keys(verifynum)
        self.br.find_element_by_name("email").send_keys(mailnum)
        sleep(1)
        self.br.find_element_by_xpath("//button[@type='submit']").click()
        sleep(2)
        # 验证学生注册
        self.br.switch_to_default_content()
        showname = self.br.find_element_by_xpath("//li[@class='name']/span")
        ActionChains(self.br).move_to_element(showname).perform()
        sleep(1)
        self.br.find_element_by_link_text("个人中心").click()
        self.br.find_element_by_link_text("个人信息").click()
        readname =self. br.find_element_by_xpath("//input[@id='username' and @class='int']").get_attribute("value")
        #
        self.assertEqual(readname,username,msg = "学生账号注册fail")
        print(readname)



    #登录验证注册的学生账号
    def test_02_login(self):                                         #登录测试用例
        self.br.find_element_by_class_name("sign ").click()
        iframe = self.br.find_element_by_id("layui-layer-iframe1")
        self.br.switch_to_frame(iframe)
        self.br.find_element_by_id("inputEmail").send_keys(username)
        sleep(1)
        self.br.find_element_by_id("inputPassword").send_keys(password)
        self.br.find_element_by_xpath("//button[@type='submit']").click()
        self.br.switch_to_default_content()
        #验证登录
        showname = self.br.find_element_by_xpath("//li[@class='name']/span")
        ActionChains(self.br).move_to_element(showname).perform()
        sleep(2)
        self.br.find_element_by_link_text("个人中心").click()
        self.br.find_element_by_link_text("个人信息").click()
        readusername = self.br.find_element_by_xpath("//input[@id='username' and @class='int']").get_attribute(
            'value')
        self.assertEqual(readusername, username, msg="学生账号登录fail")
        print(readusername)





    #注册老师账号
    def test_03_teacher_register(self):
        # 数据库删除注册用户名
        xusername1 = Deluser()
        xusername1.delusername()

        # 注册老师账号
        self. br.find_element_by_class_name("register").click()  # 点击注册按钮
        self.br.find_element_by_id("layui-layer-iframe1").click()  # 选取表单iframe1
        self.br.switch_to.default_content()
        self.br.switch_to_frame("layui-layer-iframe1")
        sleep(2)
        self.br.find_element_by_id("teacher").click()  # 默认选在学生，点击老师注册，
        self.br.find_element_by_name("username").send_keys(username)
        self.br.find_element_by_name("password").send_keys(password)
        self.br.find_element_by_name("repassword").send_keys(password)
        self.br.find_element_by_name("verify").send_keys(verifynum)
        self.br.find_element_by_name("email").send_keys(mailnum)
        sleep(1)
        self.br.find_element_by_xpath("//button[@type='submit']").click()
        sleep(1)
        self.br.switch_to.default_content()
        self.br.switch_to_frame("layui-layer-iframe2")
        self.br.find_element_by_id("name").send_keys(realchinesename)
        self.br.find_element_by_id("man").click()
        self.br.find_element_by_id("search_area_0").click()  # 选择第1个学校区域框
        self.br.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[2]/div/form/div/ul/li[3]/div/select[1]/option[10]").click()
        self.br.find_element_by_id("search_area_2").click()  # 选择第2个学校区域框
        self.br.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[2]/div/form/div/ul/li[3]/div/select[2]/option[6]").click()
        self.br.find_element_by_id("search_area_3").click()  # 选择第3个学校区域框
        qqq = self.br.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/form/div/ul/li[3]/div/select[3]/option[3]")
        ActionChains(self.br).double_click(qqq).perform()
        self.br.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/form/div/ul/li[4]/input").send_keys(shoolname)
        self.br.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/form/div/ul/li[5]/input").send_keys(mpnum)
        self.br.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/form/div/ul/li[6]/input").send_keys(QQnum)

        self.br.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/form/div/ul/div").click()
        # 验证注册
        sleep(2)

        self.br.switch_to_default_content()
        showname = self.br.find_element_by_xpath("//li[@class='name']/span")
        ActionChains(self.br).move_to_element(showname).perform()
        sleep(1)
        self.br.find_element_by_link_text("个人中心").click()
        self.br.find_element_by_link_text("个人信息").click()
        readname = self.br.find_element_by_xpath("//input[@id='username' and @class='int']").get_attribute("value")
        self.assertEqual(readname, username, msg="老师注册账号fail")
        print(readname)
    #登录验证注册的老师账号
    def test_04_login(self):                                         #登录测试用例
        self.br.find_element_by_class_name("sign ").click()
        iframe = self.br.find_element_by_id("layui-layer-iframe1")
        self.br.switch_to_frame(iframe)
        self.br.find_element_by_id("inputEmail").send_keys(username)
        sleep(1)
        self.br.find_element_by_id("inputPassword").send_keys(password)
        self.br.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/form/div/ul/li[3]/button").click()
        sleep(2)
        self.br.switch_to_default_content()
        #验证登录
        showname = self.br.find_element_by_xpath("//li[@class='name']/span")
        ActionChains(self.br).move_to_element(showname).perform()
        sleep(1)
        self.br.find_element_by_link_text("个人中心").click()
        self.br.find_element_by_link_text("个人信息").click()
        readusername = self.br.find_element_by_xpath("/html/body/div/div[1]/div/div/div[2]/div[2]/form/input[3]").get_attribute(
            'value')
        self.assertEqual(readusername, username, msg="老师账号登录fail")
        print(readusername)


if __name__ == "__main__":
    unittest.main()

