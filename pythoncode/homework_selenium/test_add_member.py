#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/28 19:59
# @Author  : tanya
# @File    : test_add_member.py
# @Software: PyCharm
import os

import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pythoncode.PO.work_weixin_index import WorkWeixinIndex
from pythoncode.PO.work_weixin_login import WorkWeixinLogin


@pytest.mark.usefixtures("print_cal")
class TestAddMember():

    func_params = {"test_add_member": ["username,account,phtone", "add_member.yml"],
                   "test_add_member_fail": ["username,account,phtone", "add_member_fail.yml"]}
    def get_params(path):
        with open(path, "r",encoding="utf-8") as f:
            params = yaml.safe_load(f)
            print(params)
        return params

    @pytest.fixture(autouse=True)
    def start_selenium(self):
        # print("debug")
        # opt = Options()
        # opt.debugger_address = "localhost:9444"
        # self.driver = webdriver.Chrome(executable_path="D:\\workspace\\pyworkspace\\chromedriver850418383.exe", options=opt)
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        self.index = WorkWeixinLogin().login()
        yield
        self.index.close()

    def test_add_member(self,username,account,phtone):
        members = self.index.add_member().add_member(username,account,phtone).get_member()
        names = [member[0] for member in members]
        assert username in names

    @pytest.mark.skip
    def test_add_member_fail(self,username,account,phtone):
        members = self.index.add_member().add_member_fail(username, account, phtone).get_member()
        print(members)