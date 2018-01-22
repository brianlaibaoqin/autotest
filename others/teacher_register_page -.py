# coding=utf-8
import pymysql
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

registername = "teatherl977"
password = "43142543"
mailnum = "2012422425@343.com"
verifynum = "hrv7"
#url = "http://www.youngmaker.com/"
url = "http://beta.youngmaker.cn/"
realchinesename = u"我的开"
shoolname = u"广西大学"
mpnum = "13612922871"
QQnum = "501023373"


fp = webdriver.FirefoxProfile("..\\firefoxPro")
br = webdriver.Firefox(fp)
br.get(url)
sleep(2)

br.find_element_by_class_name("register").click() #点击注册按钮
br.find_element_by_id("layui-layer-iframe1").click() #选取表单iframe1
br.switch_to.default_content()
br.switch_to_frame("layui-layer-iframe1")
br.find_element_by_id("teacher").click() #默认选在学生，点击老师注册，
br.find_element_by_name("username").send_keys(registername)
br.find_element_by_name("password").send_keys(password)
br.find_element_by_name("repassword").send_keys(password)
br.find_element_by_name("verify").send_keys(verifynum)
br.find_element_by_name("email").send_keys(mailnum)
br.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/form/div/ul/li[8]/button").click()
sleep(2)

br.find_element_by_id("name").send_keys(realchinesename)
br.find_element_by_id("man").click()
br.find_element_by_id("search_area_0").click() #选择第1个学校区域框
br.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/form/div/ul/li[3]/div/select[1]/option[10]").click()
br.find_element_by_id("search_area_2").click() #选择第2个学校区域框
br.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/form/div/ul/li[3]/div/select[2]/option[6]").click()
br.find_element_by_id("search_area_3").click() #选择第3个学校区域框
qqq = br.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/form/div/ul/li[3]/div/select[3]/option[3]")
ActionChains(br).double_click(qqq).perform()
br.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/form/div/ul/li[4]/input").send_keys(shoolname )
br.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/form/div/ul/li[5]/input").send_keys(mpnum)
br.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/form/div/ul/li[6]/input").send_keys(QQnum)
#br.find_element_by_xpath("//form/[@class='login-form']/div/ul/div").click()
br.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/form/div/ul/div").click()
#验证注册
sleep(2)

#iframe1 = br.find_element_by_id("iframe")
#br.switch_to_frame(iframe1)
br.switch_to_default_content()
br.find_element_by_xpath("/html/body/header/div/div/ul[2]/li[2]/span").click()
sleep(2)
br.find_element_by_link_text("个人中心").click()
br.find_element_by_link_text("个人信息").click()
readname = br.find_element_by_xpath("//input[@id='username' and @class='int']").get_attribute("value")
print(readname)
if readname == registername :
     print("老师账号注册成功，注册账号是：%s" % readname)
else:
     print("老师账号注册失败")



#js = "$('#search_area_3').val(609)"
#br.execute_script(js)

sleep(3)
br.quit()
conn = pymysql.connect(host='192.168.0.126', port=3306, user='root', passwd='mysql@youngmaker@com@2017', db='youngmaker', charset='utf8')
cur = conn.cursor()
sql = 'DELETE from`onethink_ucenter_member` WHERE `username` = %r ' %registername
try:
    cur.execute(sql)
    #提交
    conn.commit()
    print("数据库删除注册用户名ok了")
except Exception as e:
    #错误回滚
    print(e)
    print("出错了")
    conn.rollback()
finally:

    conn.close()

