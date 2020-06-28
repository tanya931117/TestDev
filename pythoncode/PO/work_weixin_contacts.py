#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/22 19:58
# @Author  : tanya
# @File    : work_weixin_contacts.py
# @Software: PyCharm
from selenium.webdriver import ActionChains

from pythoncode.PO.base_page import BasePage

class WorkWeixinContact(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#contacts"

    def import_contact(self):
        self.find(self.css_selector, ".ww_operationBar:nth-child(1) > .ww_btnWithMenu > .ww_btn_PartDropdown").click()
        self.find(self.link_text, "文件导入").click()
        from pythoncode.PO.work_weixin_import_contact import WorkWeixinImportContact
        return WorkWeixinImportContact(self._driver)

    def add_member(self):
        self.find(self.css_selector,".ww_operationBar:nth-child(1) > .js_add_member").click()
        from pythoncode.PO.work_weixin_add_member import WorkWeixinAddMember
        return WorkWeixinAddMember(self._driver)

    def get_member(self):
        mems = []
        ##姓名
        els = self.finds(self.css_selector, f".member_colRight_memberTable_td:nth-child(2)")
        for e in els :
            mem = []
            title = e.get_attribute("title")
            mem.append(title)
            mems.append(mem)

        for i in range(3,7):
            els = self.finds(self.css_selector,f".member_colRight_memberTable_td:nth-child({i})")
            for j in range(len(els)):
                mem = mems[j]
                e = els[j]
                title = e.get_attribute("title")
                mem.append(title)
        return mems

