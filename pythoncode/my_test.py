#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/12 22:49
# @Author  : tanya
# @File    : my_test.py
# @Software: PyCharm
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pythoncode.PO.work_weixin_contacts import WorkWeixinContact
from pythoncode.PO.work_weixin_index import WorkWeixinIndex
from pythoncode.my_utils import get_path


class MyTest():
    @pytest.fixture(autouse=True)
    def set_driver_debug(self):
        print("debug")
        opt = Options()
        opt.debugger_address = "localhost:9444"
        self.driver = webdriver.Chrome(executable_path="D:\\workspace\\pyworkspace\\chromedriver.exe", options=opt)
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        yield
        self.driver.quit()

    @pytest.mark.skip
    def test_get_member(self):
        mems = WorkWeixinContact(self.driver).get_member()
        print(mems)
    @pytest.mark.skip
    def test_import(self):
        root = get_path.get_root_Path()
        file_path = os.path.join(root,"import_contact_template.xlsx")
        mems = WorkWeixinIndex(self.driver).import_contact().upload(file_path).get_member()
        print(mems)

    @pytest.mark.skip
    def test_import_index(self):
        root = get_path.get_root_Path()
        file_path = os.path.join(root,"import_contact_template.xlsx")
        WorkWeixinIndex(self.driver).import_contact().upload(file_path)

    @pytest.mark.skip
    def test_import_unvalid_index(self):
        root = get_path.get_root_Path()
        file_path = os.path.join(root, "test.gif")
        file = WorkWeixinIndex(self.driver).import_contact().upload_unvalid(file_path)
        assert file=="test.gif"

    @pytest.mark.skip
    def test_index_import_empty(self):
        root = get_path.get_root_Path()
        file_path = os.path.join(root,"empty.xlsx")
        title = WorkWeixinIndex(self.driver).import_contact().upload_empty(file_path)
        assert title=="通讯录上传未成功"

    def test_add_member(self):
        members = WorkWeixinIndex(self.driver).add_member().add_member("银赫","eunhyuk","13500000000").get_member()
        print(members)

if __name__=="__main__":
    print(os.environ["using_headless"])
