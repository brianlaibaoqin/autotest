# coding=utf-8
from time import sleep
from selenium import webdriver
from data.datainfo import url
from function.base.mySQLDB import DB
import os

db = DB('120.79.13.73', 3306, 'root', 'root', 'ymtest')
username = "autotest11 "
strSql = 'DELETE from`onethink_ucenter_member` WHERE `username` = %r ' % username
db.update(strSql)

fp = webdriver.FirefoxProfile("D:\\youngmaker_auto\\function\\firefoxPro")
driver = webdriver.Firefox(fp)
driver.implicitly_wait(10)
driver.get(url)
driver.maximize_window()
driver.find_element_by_link_text(u"编程").click()
sleep(30)
os.system("C:\\Users\\Administrator\\Desktop\\tea_register.exe")
driver.refresh()
all_handles = driver.window_handles
print(all_handles)
print(all_handles[0])
print(all_handles[1])
bb = driver.title
print(bb)
driver.quit()