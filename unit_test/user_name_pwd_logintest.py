# -*- encoding:utf8 -*-
import ddt
import unittest
from time import sleep
from selenium import webdriver
from function.base.Excel import ExcelUtil
import time
from function.base.html_test_runner import HtmlTestRunner
from data.datainfo import *
from selenium.webdriver.common.action_chains import ActionChains

a = ExcelUtil()
p = a.next()

@ddt.ddt
class Test_excellogin(unittest.TestCase):
    """ EXCEl数据的登录测试"""
    def setUp(self):
        fp = webdriver.FirefoxProfile(path)
        self.driver = webdriver.Firefox(fp)
        self.driver.implicitly_wait(30)
        self.driver.get(url)

    def tearDown(self):
        self.driver.quit()
        pass
    def user_login(self,username, password):
        self.driver.find_element_by_class_name("sign ").click()
        iframe = self.driver.find_element_by_id("layui-layer-iframe1")
        self.driver.switch_to_frame(iframe)
        self.driver.find_element_by_id("inputEmail").send_keys(username)
        sleep(1)
        self.driver.find_element_by_id("inputPassword").send_keys(password)
        self.driver.find_element_by_xpath("//*[@class='inputTxt int4'and @type='submit']").click()
        sleep(3)
    # 退出
    def user_logout(self):
        self.driver.quit()
    def v_stu_login_suc(self):
        self.driver.switch_to_default_content()
        per_center = self.driver.find_element_by_xpath("//li[@class='name']/span")
        ActionChains(self.driver).double_click(per_center).perform()
        sleep(3)
        self.driver.find_element_by_link_text("个人中心").click()
        self.driver.find_element_by_link_text("个人信息").click()
        try:
            readusername = self.driver.find_element_by_xpath(
                "/html/body/div/div[1]/div/div/div[2]/div[2]/form/input[3]").get_attribute(
                'value')
            return readusername
        except:
            return False

    @ddt.data(*p)
    def test_1(self,data):
        """ EXCEl登录测试"""
        print(data)
        username = data[1]
        password = data[2]
        status = data[3]
        self.user_login(username,password)
        sleep(2)
        try:
            if status == True:
                userinfo = self.v_stu_login_suc()
                self.assertTrue(userinfo,data[4])
                print("登录成功",userinfo)
            else:
                sleep(1)
                fail_msg = self.driver.find_element_by_xpath("//*[@id='body']/div[2]/div[1]/form/div/ul/li[1]/p").text
                print(fail_msg)
                self.assertIn(data[4],fail_msg)
        except Exception as ErrMsg:
            self.assertEqual("",ErrMsg)
if __name__ == "__main__":
    aa = unittest.makeSuite(Test_excellogin)
    filename = "D:\\youngmaker_auto\\report\\" + time.strftime("%Y-%m-%d %H_%M_%S") + "result.html"  # 测试结果存储路径
    path = open(filename, "wb")  # 自动生成测试报告
    runner = HtmlTestRunner(stream=path,
                                title="登录测试结果",
                                description="用例执行结果:")  # 测试用例编辑

    runner.run(aa)