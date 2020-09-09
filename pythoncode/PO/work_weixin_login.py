#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/20 18:59
# @Author  : tanya
# @File    : work_weixin_login.py
# @Software: PyCharm

import os
from pythoncode.PO.base_page import BasePage
from pythoncode.PO.work_weixin_index import WorkWeixinIndex
from pythoncode.PO.work_weixin_register import WorkWeixinRegister
from pythoncode.my_utils.get_path import get_root_Path


class WorkWeixinLogin(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome_baidu"

    def goto_register(self):
        self.find(self.css_selector,".login_registerBar_link").click()
        return WorkWeixinRegister(self._driver)

    def login(self):
        file_path = os.path.join(get_root_Path(), "cookies.json")
        self.add_cookie(file_path)
        self.refresh()
        self.wait_default(10,"clickable",self.id,"menu_index")
        return WorkWeixinIndex(self._driver)