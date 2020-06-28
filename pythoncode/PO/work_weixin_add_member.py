#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/26 19:31
# @Author  : tanya
# @File    : work_weixin_add_member.py
# @Software: PyCharm
from selenium.common.exceptions import NoSuchElementException

from pythoncode.PO.base_page import BasePage
from pythoncode.PO.work_weixin_contacts import WorkWeixinContact


class WorkWeixinAddMember(BasePage):
    def add_member(self,username,account,phone):
        self.find(self.id,"username").send_keys(username)
        self.find(self.id, "memberAdd_acctid").send_keys(account)
        self.find(self.id, "memberAdd_phone").send_keys(phone)
        self.find(self.css_selector,".js_member_editor_form > .ww_operationBar:nth-child(1) > .js_btn_save").click()
        return WorkWeixinContact(self._driver)

    def add_member_fail(self,username,account,phone):
        if username is not None:
            self.find(self.id,"username").send_keys(username)
        if account is not None:
            self.find(self.id, "memberAdd_acctid").send_keys(account)
        if phone is not None:
            self.find(self.id, "memberAdd_phone").send_keys(phone)
        self.find(self.css_selector,".js_member_editor_form > .ww_operationBar:nth-child(1) > .js_btn_save").click()
        self.find(self.css_selector, ".js_member_editor_form > .ww_operationBar:nth-child(1) > .js_btn_cancel").click()
        try:
            leave = self.find(self.css_selector, ".ww_dialog_foot > .ww_btn:nth-child(2)")
        except NoSuchElementException:
            return WorkWeixinContact(self._driver)
        if leave is not None:
            leave.click()
        return WorkWeixinContact(self._driver)