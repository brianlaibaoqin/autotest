# coding=utf-8
from time import sleep
from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys
from function.base.html_test_runner import HtmlTestRunner
username = "laibaoqin"             # 登录账号
Password = "a124689a"              # 登录密码
url = "http://www.youngmaker.com/" #登录网址

class login(unittest.TestCase):
    def setUp(self):                                   # 打开登录页面
        fp = webdriver.FirefoxProfile("..\\firefoxPro")
        self.br = webdriver.Firefox(fp)
        self.br.implicitly_wait(10)
        self.br.get(url)

    def test_login(self):                                         #登录测试用例
        self.br.find_element_by_class_name("sign ").click()
        iframe = self.br.find_element_by_id("layui-layer-iframe1")
        self.br.switch_to_frame(iframe)
        self.br.find_element_by_id("inputEmail").send_keys(username)
        self.br.find_element_by_id("inputPassword").send_keys(Password)
        self.br.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/form/div/ul/li[3]/button").click()
        sleep(2)
        #验证登录
        self.br.find_element_by_xpath("/html/body/header/div/div/ul[2]/li[2]/span").click()
        sleep(2)
        self.br.find_element_by_link_text("个人中心").click()
        self.br.find_element_by_link_text("个人信息").click()
        readusername = self.br.find_element_by_xpath("/html/body/div/div[1]/div/div/div[2]/div[2]/form/input[3]").get_attribute(
            'value')
        print(readusername)
        if readusername == username:
            print("登录成功，登录账号是：%s" % readusername)
        else:
            print("登录失败")

    def tearDown(self):
        self.br.quit()
        print("关闭浏览器")

if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(login("test_login"))
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = "D:\\Autotest\\report\\" + now + "result.html" #测试结果存储路径

    path = open(filename,"wb")      #自动生成测试报告
    runner = HtmlTestRunner(stream = path,title="登录测试结果",description="用例执行结果:") #测试用例便捷
    runner.run(suite) #执行测试用例
    path.close() #关闭测试报告
    print("测试结束")

