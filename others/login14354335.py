# coding=utf-8
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

username = "laibaoqin"
password = "a124689a"
#url = "http://www.youngmaker.com/"
url = "http://beta.youngmaker.cn/"
fp = webdriver.FirefoxProfile("..\\firefoxPro")
br = webdriver.Firefox(fp)
br.get(url)
sleep(4)
br.find_element_by_class_name("sign ").click()
iframe = br.find_element_by_id("layui-layer-iframe1")
br.switch_to_frame(iframe)
br.find_element_by_id("inputEmail").send_keys(username)
br.find_element_by_id("inputPassword").send_keys(password)
br.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/form/div/ul/li[3]/button").click()
sleep(2)
#验证登录功能
br.find_element_by_xpath("/html/body/header/div/div/ul[2]/li[2]/span").click()
sleep(2)
br.find_element_by_link_text("个人中心").click()
br.find_element_by_link_text("个人信息").click()
read = br.find_element_by_xpath("/html/body/div/div[1]/div/div/div[2]/div[2]/form/input[3]").get_attribute('value')
print(read)
if read == username:
    print("登录成功")
else:
    print("登录失败")
br.quit()





