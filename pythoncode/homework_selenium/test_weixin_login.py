#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/16 21:54
# @Author  : tanya
# @File    : test_weixin_login.py
# @Software: PyCharm
import json
import os
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pythoncode.PO.work_weixin_login import WorkWeixinLogin
from pythoncode.my_utils.get_path import get_root_Path


@pytest.mark.usefixtures("print_cal")
class TestLoginReuse():

    @pytest.fixture()
    def set_driver_debug(self):
        opt = Options()
        opt.debugger_address="localhost:9333"
        self.driver = webdriver.Chrome(executable_path="D:\\workspace\\pyworkspace\\chromedriver850418383.exe",options=opt)
        yield
        self.driver.quit()

    @pytest.fixture()
    def set_driver_cookie(self):
        try:
            using_headless = os.environ["using_headless"]
        except KeyError:
            using_headless = None
            print("未配置环境变量using_headless，按照有界面方式运行UI自动化测试")
        options = Options()
        if using_headless is not None and using_headless.lower() == "true":
            print("使用无界面方式运行")
            options.add_argument("--headless")
        self.driver = webdriver.Chrome("D:\\workspace\\pyworkspace\\chromedriver850418383.exe",options=options)
        yield
        self.driver.quit()

    @pytest.mark.skip
    def test_login_debug(self,set_driver_debug):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        element_index = WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.ID,"menu_index")))
        if element_index is not None:
            print("跳过扫码成功")
            cookies = self.driver.get_cookies()
            with open(os.path.join(get_root_Path(),"cookies.json"),"w") as f:
                json.dump(cookies,f)
            assert True

    def test_login_cookie(self,set_driver_cookie):
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        file_path = os.path.join(get_root_Path(), "cookies.json")
        with open(file_path, "r") as f:
            cookies = json.load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        while True:
            self.driver.refresh()
            element_index = WebDriverWait(self.driver, 10).until(
                expected_conditions.element_to_be_clickable((By.ID, "menu_index")))
            if element_index is not None:
                break
        assert True



