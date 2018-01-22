# -*- coding:utf-8 -*-
import os
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

"""
练习启动各种浏览器：Firefox， Chrome， IE
练习启动各种浏览器的同时加载插件：Firefox， Chrome， IE
"""


def start_firefox_with_default_settings():
    """启动Firefox浏览器， 使用本地配置文件中的选项配置浏览器
    自动将页面载入过程导出为Har文件，并存放在
    配置项 extensions.firebug.netexport.defaultLogDir指定的D:\temp\selenium2目录下
    """
    firefox_bin = os.path.abspath(r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe")
    os.environ["webdriver.firefox.bin"] = firefox_bin

    # 使用从别的机器上拷贝来的浏览器配置
    #firefox_profile = webdriver.FirefoxProfile(os.path.abspath(r"D:\Temp\selenium2\Profiles\mm9zxom8.default"))
    # 使用本地的默认配置
    firefox_profile = webdriver.FirefoxProfile("C:\\Users\\Administrator\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\1s41a9dg.default")
    driver = webdriver.Firefox(firefox_profile=firefox_profile)
    driver.get("http://www.baidu.com")

    '''
    driver.close()
    driver.quit()
    driver = None
    '''


if __name__ == "__main__":
    start_firefox_with_default_settings()