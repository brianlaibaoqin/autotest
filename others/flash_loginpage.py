# coding=utf-8
from time import sleep
from selenium import webdriver
from data.datainfo import url
import os


fp = webdriver.FirefoxProfile("C:\\Users\\Administrator\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\atbkf7sg.default")
fp.set_preference("plugin.state.flash",2)
driver = webdriver.Firefox(fp)
driver.implicitly_wait(10)
driver.get(url)
driver.maximize_window()
driver.find_element_by_link_text(u"编程").click()
sleep(30)
all_handles = driver.window_handles
Cur = driver.current_window_handle
driver.switch_to_window(all_handles[1])
print(all_handles)
print(all_handles[0])
print(all_handles[1])

bb = driver.title
print(bb)
os.system("C:\\Users\\Administrator\\Desktop\\testcase.exe")
driver.refresh()
all_handles2 = driver.window_handles
print(all_handles2)
print(all_handles2[0])
print(all_handles2[1])
print(all_handles2[2])
driver.switch_to_window(all_handles2[2])
try:
    flash_username = driver.find_element_by_xpath("//*[@id='head']/ul[2]/li[2]/span").text
    if flash_username !="":
        print("flash页面登录测试成功",flash_username)
    else:
        print("flash页面登录测试失败", flash_username)
except:
    print("测试出错了")
driver.quit()

