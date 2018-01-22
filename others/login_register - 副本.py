# coding=utf-8
from time import sleep
from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys
from function.base.html_test_runner import HtmlTestRunner
import pymysql
from selenium.webdriver.common.action_chains import ActionChains
from function.base.mySQLDB import DB
username = "autotest"             #登录账号
password = "a124689a"               #登录密码
#url = "http://www.youngmaker.com/" #登录网址
url = "http://beta.youngmaker.cn/" #登录网址
mailnum = "autotest110@343.com"    #邮箱
teachername = " 2017112820510"     #老师创客号
verifynum = "hrv7"                 #万能码
realchinesename = u"我的开"         #真实中文名
shoolname = u"广西大学"             #学校
mpnum = "13612922871"              #手机
QQnum = "501023373"                #QQ号



class login(unittest.TestCase):
    def setUp(self):                                   # 打开登录页面
         fp = webdriver.FirefoxProfile("..\\firefoxPro")
         self.br = webdriver.Firefox(fp)
         self.br.implicitly_wait(10)
         self.br.get(url)
    #注册学生账号
    def test_01_student_register(self):

        deluser = DB('192.168.0.126',3306,'root','mysql@youngmaker@com@2017','youngmaker')
        strSql = 'DELETE from`onethink_ucenter_member` WHERE `username` = %r ' % username
        deluser.update(strSql)



        self.br.find_element_by_class_name("register").click()  # 点击注册按钮
        self.br.find_element_by_id("layui-layer-iframe1").click()  # 选取表单iframe1
        self.br.switch_to.default_content()
        self.br.switch_to_frame("layui-layer-iframe1")
        self.br.find_element_by_name("username").send_keys(username)
        self.br.find_element_by_name("password").send_keys(password)
        self.br.find_element_by_name("repassword").send_keys(password)
        self.br.find_element_by_name("verify").send_keys(verifynum)
        self.br.find_element_by_name("email").send_keys(mailnum)
        # self.br.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/form/div/ul/li[7]/input").send_keys(teachername)
        self.br.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/form/div/ul/li[8]/button").click()
        sleep(2)
        # 验证学生注册
        self.br.switch_to_default_content()
        self.br.find_element_by_xpath("/html/body/header/div/div/ul[2]/li[2]/span").click()
        sleep(2)
        self.br.find_element_by_link_text("个人中心").click()
        self.br.find_element_by_link_text("个人信息").click()
        readname =self. br.find_element_by_xpath("//input[@id='username' and @class='int']").get_attribute("value")
        print(readname)
        if readname == username:
            print("学生账号注册成功，注册账号是：%s" % readname)
        else:
            print("学生账号注册失败")
        sleep(3)


    #登录验证注册的学生账号
    def test_02_login(self):                                         #登录测试用例
        self.br.find_element_by_class_name("sign ").click()
        iframe = self.br.find_element_by_id("layui-layer-iframe1")
        self.br.switch_to_frame(iframe)
        self.br.find_element_by_id("inputEmail").send_keys(username)
        self.br.find_element_by_id("inputPassword").send_keys(password)
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
            print("学生账号登录成功，登录账号是：%s" % readusername)
        else:
            print("登录失败")




    #注册老师账号
    def test_03_teacher_register(self):
        # 数据库删除注册用户名
        deluser = DB('192.168.0.126',3306,'root','mysql@youngmaker@com@2017','youngmaker')
        strSql = 'DELETE from`onethink_ucenter_member` WHERE `username` = %r ' % username
        deluser.update(strSql)

        # 注册老师账号
        self. br.find_element_by_class_name("register").click()  # 点击注册按钮
        self.br.find_element_by_id("layui-layer-iframe1").click()  # 选取表单iframe1
        self.br.switch_to.default_content()
        self.br.switch_to_frame("layui-layer-iframe1")
        self.br.find_element_by_id("teacher").click()  # 默认选在学生，点击老师注册，
        self.br.find_element_by_name("username").send_keys(username)
        self.br.find_element_by_name("password").send_keys(password)
        self.br.find_element_by_name("repassword").send_keys(password)
        self.br.find_element_by_name("verify").send_keys(verifynum)
        self.br.find_element_by_name("email").send_keys(mailnum)
        self.br.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/form/div/ul/li[8]/button").click()
        sleep(2)

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
        self.br.find_element_by_xpath("/html/body/header/div/div/ul[2]/li[2]/span").click()
        sleep(2)
        self.br.find_element_by_link_text("个人中心").click()
        self.br.find_element_by_link_text("个人信息").click()
        readname = self.br.find_element_by_xpath("//input[@id='username' and @class='int']").get_attribute("value")
        print(readname)
        if readname == username:
            print("老师账号注册成功，注册账号是：%s" % readname)
        else:
            print("老师账号注册失败")

    #登录验证注册的老师账号
    def test_04_login(self):                                         #登录测试用例
        self.br.find_element_by_class_name("sign ").click()
        iframe = self.br.find_element_by_id("layui-layer-iframe1")
        self.br.switch_to_frame(iframe)
        self.br.find_element_by_id("inputEmail").send_keys(username)
        self.br.find_element_by_id("inputPassword").send_keys(password)
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
            print("老师账号登录成功，登录账号是：%s" % readusername)
        else:
            print("登录失败")

    def tearDown(self):
        self.br.quit()
        print("关闭浏览器")

if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(login("test_01_student_register"))
    suite.addTest(login("test_02_login"))
    suite.addTest(login("test_03_teacher_register"))
    suite.addTest(login("test_04_login"))
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = "D:\\youngmaker_auto\\report\\" + now + "result.html" #测试结果存储路径

    path = open(filename,"wb")      #自动生成测试报告
    runner = HtmlTestRunner(stream = path,title="登录测试结果",description="用例执行结果:") #测试用例编辑
    runner.run(suite) #执行测试用例
    path.close() #关闭测试报告
    print("测试结束")

