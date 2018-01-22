import unittest
import time
from function.base.html_test_runner import HtmlTestRunner
from suite.login_testsuit import LoginSuit
from unit_test.user_name_pwd_logintest import Test_excellogin
from unit_test.scratchPagelogin_register import Flashpage_reg_login

class YoungMKTestRunner():
    def run_tests(self):
        # 创建一个测试套件
        aa = unittest.TestSuite()
        # 在测试套件中添加需要运行的测试用例
        aa = LoginSuit(aa).add_tests()
        bb = unittest.makeSuite(Test_excellogin)
        cc = unittest.makeSuite(Flashpage_reg_login)

        self.filename = "D:\\youngmaker_auto\\report\\" + time.strftime("%Y-%m-%d %H_%M_%S") + "result.html"  # 测试结果存储路径
        path = open(self.filename, "wb")  # 自动生成测试报告
        runner = HtmlTestRunner(stream=path,
                                title="登录测试结果",
                                description="用例执行结果:")  # 测试用例编辑
        runner.run(cc)  # 执行测试用例
        runner.run(aa)  # 执行测试用例
        runner.run(bb)  # 执行测试用例
        path.close()  # 关闭测试报告
if __name__ == "__main__":
     start = YoungMKTestRunner()
     start.run_tests()
     print("测试结束")

