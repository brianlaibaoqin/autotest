# -*- coding: utf-8 -*-
from selenium.webdriver.support.select import Select
from function.base.base_page import *
from function.page.login_page import RanzhiLogin
import unittest
from time import sleep

#这个类封装了产品的功能
class RanzhiProduct(RanzhiLogin):
    rzDb = None
    #构造函数
    def __init__(self):
        super(RanzhiProduct, self).__init__()   #调用父类的构造函数
        self.init_db()                          #相比父类加一个操作
    #析造函数
    def __del__(self):
        pass

    def inputProduct(self, case):
        self.driver.find_element_by_id("name").send_keys(case[1])
        #列表元素的操作，HTML中的select标签元素操作方式如下:
        if case[2] != "":
            prodField = self.driver.find_element_by_id("line")  #产品线
            prodSelect = Select(prodField)
            prodSelect.select_by_visible_text(case[2])  #根据列表内值选择

        if case[3] != "":
            typeField = self.driver.find_element_by_id("type")  #类型
            typeSelect = Select(typeField)
            typeSelect.select_by_visible_text(case[3])  #根据列表内值选择

        if case[4] != "":
            statField = self.driver.find_element_by_id("status")  #状态
            statSelect = Select(statField)
            statSelect.select_by_visible_text(case[4])  #根据列表内值选择
     #操作产品的添加
    def ranzhi_product_add(self, case):
        try:
            self.openCrm()
            self.driver.find_element_by_link_text("产品").click()
            #self.assertIn("维护产品",  self.driver.title)
            #添加一个新产品
            self.driver.find_element_by_link_text("添加产品").click()
            sleep(1)
            self.inputProduct(case)
            self.driver.find_element_by_id("submit").click()    #保存产品
            return True
        except:
            Base.printErr("添加然之产品时失败！")
            return False
    #验证一下产品添加是否成功
    def ranzhi_product_add_v(self, case):
        try:
            #界面验证
            if case[5]:
                sleep(2)
                #验证产品列表是否保存成功
                prodName = self.driver.find_element_by_xpath("//table[@id='productList']/tbody/tr[1]/td[2]").text
                unittest.TestCase().assertEqual(case[1], prodName)
            else:
                actual = self.driver.find_element_by_id("nameLabel").text
                unittest.TestCase().assertIn(case[6], actual)
            #数据库验证
            dbrc = self.rzDB.execSql(case[8], True)
            if dbrc[0] == False:
                return "ERR--数据库操作失败，信息：%s"%dbrc[1]
            else:
                if dbrc[1] != 1:
                    return "FAIL--数据库验证返回False!"
        except:
            return Base.printErr("ERR--验证然之产品添加时失败！", False)
        return "PASS--产品添加/验证成功：%s"%case[1]

#开始写调试代码，调试上面的产品类
if __name__=='__main__':
    rzProduct = RanzhiProduct()
    ex = g_dicFun.get("excel")

    #用例一：正确的产品添加，用例执行成功
    print("----正确的产品添加及验证-----")
    case = ["正确的产品添加1","51测试产品",\
            "51测试产品线","服务类","正常",True,"",\
            "delete from ranzhi.sys_product where name = '51测试产品'"\
            ,"select count(*)=1 from sys_product where name='51测试产品'"
             "and status='normal' and type='service' and line='aa'","",""]

    s =  ex.str_parse_func(case[7])
    rzProduct.rzDB.execSql(s)
    rzProduct.log_in(g_dicRanzhi.get("user"), g_dicRanzhi.get("password"))
    rzProduct.ranzhi_product_add(case)
    print(rzProduct.ranzhi_product_add_v(case))
    rzProduct.close_driver()

    #用例二：产品名称为空的添加，用例会执行成功
    print("----产品名称为空的添加-----")
    case = ["产品名称为空","",\
            "51测试产品线","服务类","正常",False,"名称不能为空。",\
            "$sql.delProduct()"\
            ,"select count(*)=0 from sys_product where name=''" \
             ,"",""]
    s =  ex.str_parse_func(case[7])
    rzProduct.rzDB.execSql(s)
    rzProduct.log_in(g_dicRanzhi.get("user"), g_dicRanzhi.get("password"))
    rzProduct.ranzhi_product_add(case)
    print(rzProduct.ranzhi_product_add_v(case))
    rzProduct.close_driver()

    #用例三：产品名称0的添加，期望是可以保存的，实际此处无法保存
    print("-----产品名称0的添加-----")
    case = ["产品名称为0","0",\
            "51测试产品线","服务类","正常",True,"",\
            "$sql.delProduct(0)"\
            ,"select count(*)=0 from sys_product where name='0'"
             "and status='normal' and type='service' and line='cc'","",]
    s =  ex.str_parse_func(case[7])
    rzProduct.rzDB.execSql(s)
    rzProduct.log_in(g_dicRanzhi.get("user"), g_dicRanzhi.get("password"))
    rzProduct.ranzhi_product_add(case)
    print(rzProduct.ranzhi_product_add_v(case))
    rzProduct.close_driver()
