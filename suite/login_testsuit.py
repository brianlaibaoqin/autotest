# coding=utf-8
from unit_test.login_register import login
from unit_test.bugverfy import BugloginV
from unit_test.homepage_login import Hp_login
from unit_test.homepage_loginpop import Hp_loginpop
from unit_test.homepage_student_registerpop import Hp_stu_registerpop
from unit_test.homepage_teacher_registerpop import Hp_tea_registerpop


class LoginSuit():
    def __init__(self,testSuit):
        self.testSuit = testSuit
    def add_tests(self):

        self.testSuit.addTest(login("test_01_student_register"))
        self.testSuit.addTest(login("test_02_login"))
        self.testSuit.addTest(login("test_03_teacher_register"))
        self.testSuit.addTest(login("test_04_login"))
        self.testSuit.addTest(BugloginV("test_01_step1"))
        self.testSuit.addTest(BugloginV("test_02_step2"))
        self.testSuit.addTest(BugloginV("test_03_step3"))
        self.testSuit.addTest(Hp_login("test_01"))
        self.testSuit.addTest(Hp_login("test_02"))
        self.testSuit.addTest(Hp_login("test_03"))
        self.testSuit.addTest(Hp_login("test_04"))
        self.testSuit.addTest(Hp_loginpop("test_01"))
        self.testSuit.addTest(Hp_loginpop("test_02"))
        self.testSuit.addTest(Hp_loginpop("test_03"))
        self.testSuit.addTest(Hp_loginpop("test_04"))
        self.testSuit.addTest(Hp_stu_registerpop("test_01"))
        self.testSuit.addTest(Hp_stu_registerpop("test_02"))
        self.testSuit.addTest(Hp_stu_registerpop("test_03"))
        self.testSuit.addTest(Hp_stu_registerpop("test_04"))
        self.testSuit.addTest(Hp_tea_registerpop("test_01"))
        self.testSuit.addTest(Hp_tea_registerpop("test_02"))
        self.testSuit.addTest(Hp_tea_registerpop("test_03"))
        self.testSuit.addTest(Hp_tea_registerpop("test_04"))
        return self.testSuit
















