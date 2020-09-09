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
from pythoncode.PO.work_weixin_login import WorkWeixinLogin
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
        # print("debug")
        # opt = Options()
        # opt.debugger_address = "localhost:9444"
        # self.driver = webdriver.Chrome(executable_path="D:\\workspace\\pyworkspace\\chromedriver850418383.exe", options=opt)
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        # self.driver = webdriver.Chrome(executable_path="D:\\workspace\\pyworkspace\\chromedriver850418383.exe")
        self.index = WorkWeixinLogin().login()
        yield
        self.index.close()

    def test_index_import_empty(self,file_name):
        root = get_path.get_root_Path()
        file_path = os.path.join(root,file_name)
        title = self.index.import_contact().upload_empty(file_path)
        assert title=="通讯录上传未成功"

    def test_index_import(self,file_name,check_data):
        root = get_path.get_root_Path()
        file_path = os.path.join(root,file_name)
        mems = self.index.import_contact().upload(file_path).get_member()
        names = [mem[0] for mem in mems]
        check_names = [data[0] for data in check_data]
        assert set(check_names).issubset(set(names))

    def test_index_import_unvalid(self,file_name):
        root = get_path.get_root_Path()
        file_path = os.path.join(root,file_name)
        text = self.index.import_contact().upload_unvalid(file_path)
        assert text=="将文件拖拽至此区域"