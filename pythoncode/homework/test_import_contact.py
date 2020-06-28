#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/26 16:36
# @Author  : tanya
# @File    : test_import_contact.py
# @Software: PyCharm
import os

import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pythoncode.PO.work_weixin_index import WorkWeixinIndex
from pythoncode.my_utils import get_path

@pytest.mark.usefixtures("print_cal")
class TestImportContact():

    func_params = {"test_index_import": ["file_name,check_data", "import_case.yml"],
                   "test_index_import_empty": ["file_name", "import_empty_case.yml"],
                   "test_index_import_unvalid": ["file_name", "import_unvalid_case.yml"]}
    def get_params(path):
        with open(path, "r",encoding="utf-8") as f:
            params = yaml.safe_load(f)
            print(params)
        return params

    @pytest.fixture(autouse=True)
    def start_selenium(self):
        print("debug")
        opt = Options()
        opt.debugger_address = "localhost:9444"
        self.driver = webdriver.Chrome(executable_path="D:\\workspace\\pyworkspace\\chromedriver.exe", options=opt)
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        yield
        self.driver.quit()

    def test_index_import_empty(self,file_name):
        root = get_path.get_root_Path()
        file_path = os.path.join(root,file_name)
        title = WorkWeixinIndex(self.driver).import_contact().upload_empty(file_path)
        assert title=="通讯录上传未成功"

    def test_index_import(self,file_name,check_data):
        root = get_path.get_root_Path()
        file_path = os.path.join(root,file_name)
        mems = WorkWeixinIndex(self.driver).import_contact().upload(file_path).get_member()
        for mem in mems:
            if mem[0] == check_data[0]:
                assert True
                break
        else:
            assert False

    def test_index_import_unvalid(self,file_name):
        root = get_path.get_root_Path()
        file_path = os.path.join(root,file_name)
        text = WorkWeixinIndex(self.driver).import_contact().upload_unvalid(file_path)
        assert text=="将文件拖拽至此区域"