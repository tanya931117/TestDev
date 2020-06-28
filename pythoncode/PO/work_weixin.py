#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/20 18:54
# @Author  : tanya
# @File    : work_weixin.py
# @Software: PyCharm

from pythoncode.PO.base_page import BasePage
from pythoncode.PO.work_weixin_login import WorkWeixinLogin
from pythoncode.PO.work_weixin_register import WorkWeixinRegister


class WorkWeixin(BasePage):
    _base_url = "https://work.weixin.qq.com/"

    def goto_login(self):
        self.find(self.css_selector,".index_top_operation_loginBtn").click()
        return WorkWeixinLogin(self._driver)

    def goto_register(self):
        self.find(self.css_selector,".index_head_info_pCDownloadBtn").click()
        return WorkWeixinRegister(self._driver)

