#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/20 18:22
# @Author  : tanya
# @File    : base_page.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage():
    _base_url=""
    def __init__(self,driver:WebDriver):
        self._driver = None
        if self._driver is None:
            _driver = webdriver.Chrome("D:\\workspace\\pyworkspace\\chromedriver.exe")
        else:
            _driver = driver
        if self._base_url != "":
            self._driver.get(self._base_url)

    def find(self,by,locator):
        return self._driver.find_element(by,locator)