# coding=utf-8
from time import sleep
from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from data.datainfo import *
from selenium.webdriver.support.ui import WebDriverWait



class BugloginV(unittest.TestCase):
    """ 登录bugs的验证"""
    def setUp(self):               # 打开登录页面
         fp = webdriver.FirefoxProfile(path)
         fp.set_preference("plugin.state.flash", 2)
         self.br = webdriver.Firefox(fp)
         self.br.implicitly_wait(30)
         self.br.get(url)

    def tearDown(self):
         self.br.quit()
         pass

    def test_01_step1(self):
        '''点击特色课程，Scratch初体验login'''
        aa = self.br.find_element_by_xpath("//li[@class='li1']/p[1]")
        self.br.execute_script("arguments[0].scrollIntoView(false);",aa)
        sleep(2)
        self.br.find_element_by_xpath("//li[@class='li1']/p[1]").click()
        self.br.find_element_by_xpath("//div[@id='body']/div/ul/li[1]/div/h4").click()
        bb = self.br.find_element_by_xpath("//div[@class='layui-layer-content']/iframe")
        self.br.switch_to_frame(bb)
        self.br.find_element_by_xpath("//input[@id='inputEmail' and @class='span3 fl']").clear()
        self.br.find_element_by_xpath("//input[@id='inputEmail' and @class='span3 fl']").send_keys(username)
        sleep(1)
        self.br.find_element_by_xpath("//input[@id='inputPassword' and @class='span3 fl']").clear()
        self.br.find_element_by_xpath("//input[@id='inputPassword' and @class='span3 fl']").send_keys(password)
        sleep(1)
        self.br.find_element_by_xpath("//*[@class='inputTxt int4']").click()
        sleep(2)
        self.br.switch_to_default_content() #换了selenium3.5版本就必须加这句
        sleep(2)
        try:
            readname =self.br.find_element_by_xpath("//*[@id='head']/ul[2]/li[2]/span").text
            self.assertTrue(readname, username)
        except Exception as msg:
            print(msg)
            self.br.get_screenshot_as_file("D\\youngmaker_auto\\report\\" + time.strftime("%Y-%m-%d %H_%M_%S") + "test_01_step1msg.jpg")

    def test_02_step2(self):
        '''登陆bug验证步骤2，点击菜单学生作品，点赞'''

        self.br.find_element_by_xpath("//*[@id='mycode_lists']/a").click()
        cur_handle1 =self.br.current_window_handle
        self.br.find_element_by_xpath("//a[@href='/home/mycode/detail/id/3533.html']/h4").click()
        sleep(1)
        all_handles = self.br.window_handles
        print(all_handles)
        self.br.switch_to_window(all_handles[1])
        sleep(2)
        bb = self.br.find_element_by_xpath("//*[@id='body']/div/div[2]/ul/li[1]/span")
        self.br.execute_script("arguments[0].scrollIntoView(false);",bb)
        sleep(2)
        WebDriverWait(self.br,15).until(lambda x: x.find_element_by_xpath("//span[@class='spanImg1']")).click()   #点击赞

        iframe = self.br.find_element_by_xpath("//*[@class='layui-layer-content']/iframe")
        self.br.switch_to_frame(iframe)
        self.br.find_element_by_xpath("//input[@id='inputEmail' and @class='span3 fl']").clear()
        self.br.find_element_by_xpath("//input[@id='inputEmail' and @class='span3 fl']").send_keys(username)
        sleep(2)
        self.br.find_element_by_xpath("//input[@id='inputPassword' and @class='span3 fl']").clear()
        self.br.find_element_by_xpath("//input[@id='inputPassword' and @class='span3 fl']").send_keys(password)
        sleep(1)
        self.br.find_element_by_xpath("//*[@class='inputTxt int4']").click()
        self.br.switch_to_default_content()  # 换了selenium3.5版本就必须加这句
        sleep(2)
        try:
            readname = self.br.find_element_by_xpath("//*[@id='head']/ul[2]/li[2]/span").text
            self.assertTrue(readname,username)
        except Exception as msg:
            print(msg)
            self.br.get_screenshot_as_file("D:\\youngmaker_auto\\report\\" + time.strftime("%Y-%m-%d %H_%M_%S") + "test_02_step2msg.jpg")

    def test_03_step3(self):
        '''登陆bug验证步骤3，点击菜单学生作品，添加留言'''
        self.br.find_element_by_xpath("//*[@id='mycode_lists']/a").click()
        cur_handle1 = self.br.current_window_handle
        self.br.find_element_by_xpath("//a[@href='/home/mycode/detail/id/3533.html']/h4").click()
        sleep(1)
        all_handles = self.br.window_handles
        self.br.switch_to_window(all_handles[1])
        sleep(2)
        bb = self.br.find_element_by_xpath("//*[@id='comment_content']")
        self.br.execute_script("arguments[0].scrollIntoView(false);", bb)
        sleep(2)
        self.br.find_element_by_xpath("//*[@id='comment_content']").send_keys("15415646fd第三方")
        cc = self.br.find_element_by_xpath("//*[@id='submit_comment']")
        self.br.execute_script("arguments[0].scrollIntoView(false);", cc)
        sleep(2)
        WebDriverWait(self.br,15).until(lambda x: x.find_element_by_xpath("//*[@id='submit_comment']")).click()
        # 点击发表
        iframe = self.br.find_element_by_xpath("//*[@class='layui-layer-content']/iframe")
        self.br.switch_to_frame(iframe)
        self.br.find_element_by_xpath("//input[@id='inputEmail' and @class='span3 fl']").clear()
        self.br.find_element_by_xpath("//input[@id='inputEmail' and @class='span3 fl']").send_keys(username)
        sleep(1)
        self.br.find_element_by_xpath("//input[@id='inputPassword' and @class='span3 fl']").clear()
        self.br.find_element_by_xpath("//input[@id='inputPassword' and @class='span3 fl']").send_keys(password)
        sleep(1)
        self.br.find_element_by_xpath("//*[@class='inputTxt int4']").click()
        self.br.switch_to_default_content()  # 换了selenium3.5版本就必须加这句
        sleep(2)
        try:
            readname = self.br.find_element_by_xpath("//*[@id='head']/ul[2]/li[2]/span").text
            print(readname)
            self.assertEqual(readname,username)
        except Exception as msg:
            print(msg)
            self.br.get_screenshot_as_file("D:\\youngmaker_auto\\report\\" + time.strftime("%Y-%m-%d %H_%M_%S") + "test_03_step3msg.jpg")


if __name__ == "__main__":
    unittest.main()