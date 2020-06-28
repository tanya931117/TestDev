#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/22 20:00
# @Author  : tanya
# @File    : work_weixin_index.py
# @Software: PyCharm
from pythoncode.PO.base_page import BasePage
from pythoncode.PO.work_weixin_add_member import WorkWeixinAddMember
from pythoncode.PO.work_weixin_contacts import WorkWeixinContact
from pythoncode.PO.work_weixin_import_contact import WorkWeixinImportContact


class WorkWeixinIndex(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_contact(self):
        self.find(self.id,"menu_contacts").click()
        return WorkWeixinContact(self._driver)

    def import_contact(self):
        self.find(self.css_selector,".index_service_cnt_itemWrap:nth-child(2)").click()
        return WorkWeixinImportContact(self._driver)

    def add_member(self):
        self.find(self.css_selector, ".index_service_cnt_itemWrap:nth-child(1)").click()
        return WorkWeixinAddMember(self._driver)