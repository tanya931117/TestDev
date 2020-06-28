#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/23 21:20
# @Author  : tanya
# @File    : work_weixin_import_contact.py
# @Software: PyCharm
from pythoncode.PO.base_page import BasePage
from pythoncode.PO.work_weixin_contacts import WorkWeixinContact


class WorkWeixinImportContact(BasePage):

    def upload(self, file_path):
        self.find(self.id, "js_upload_file_input").send_keys(file_path)
        self.wait_default(10,"clickable",self.css_selector, ".import_settingSubmit").click()
        self.wait_default(10,"clickable",self.id, "reloadContact").click()
        return WorkWeixinContact(self._driver)

    def upload_unvalid(self, file_path):
        self.wait_default(10,"presence",self.id, "js_upload_file_input").send_keys(file_path)
        return self.find(self.id, "upload_file_name").text

    def upload_empty(self, file_path):
        self.find(self.id, "js_upload_file_input").send_keys(file_path)
        self.wait_default(10, "clickable", self.css_selector, ".import_settingSubmit").click()
        return self.wait_default(10, "visibility", self.css_selector, ".import_succStage_title").text
