#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/20 18:59
# @Author  : tanya
# @File    : work_weixin_login.py
# @Software: PyCharm
from selenium.webdriver.common.by import By

from pythoncode.PO.base_page import BasePage
from pythoncode.PO.work_weixin_register import WorkWeixinRegister


class WorkWeixinLogin(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome_baidu"

    def goto_register(self):
        self.find(By.CSS_SELECTOR,".login_registerBar_link").click()
        return WorkWeixinRegister(self._driver)

    def login(self):
        print("......login...")
        return