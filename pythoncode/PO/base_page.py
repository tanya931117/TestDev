#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/20 18:22
# @Author  : tanya
# @File    : base_page.py
# @Software: PyCharm
import json
import os

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    css_selector = By.CSS_SELECTOR
    class_name = By.CLASS_NAME
    id = By.ID
    link_text = By.LINK_TEXT
    xpath = By.XPATH
    partial_link_text = By.PARTIAL_LINK_TEXT
    name = By.NAME
    tag_name = By.TAG_NAME

    _base_url=""
    def __init__(self,driver:WebDriver):
        self._driver = None
        if driver is None:
            self._driver = webdriver.Chrome("D:\\workspace\\pyworkspace\\chromedriver.exe")
        else:
            self._driver = driver
        if self._base_url != "" and self._driver is not None:
            self._driver.get(self._base_url)
        self._driver.implicitly_wait(1)

    def find(self,by,locator):
        return self._driver.find_element(by,locator)

    def finds(self,by,locator):
        return self._driver.find_elements(by,locator)

    def add_cookie(self,cookies):
        with open(cookies, "r") as f:
            cookies = json.load(f)
        for cookie in cookies:
            self._driver.add_cookie(cookie)

    def execute_js(self,js,*args):
        self._driver.execute_script(js,*args)

    def get_cookie(self,cookie_file):
        cookies = self._driver.get_cookies()
        with open(cookie_file, "w") as f:
            json.dump(cookies, f)

    def refresh(self):
        self._driver.refresh()

    def wait_default(self,seconds,method:str,by,locator):
        el = None
        if method == "clickable":
            el = WebDriverWait(self._driver, seconds).until(
                method=expected_conditions.element_to_be_clickable((by, locator)))
        elif method == "visibility":
            el = WebDriverWait(self._driver, seconds).until(
                method=expected_conditions.visibility_of_element_located((by, locator)))
        elif method == "presence":
            el = WebDriverWait(self._driver, seconds).until(
                method=expected_conditions.presence_of_element_located((by, locator)))
        return el

    def wait_custom(self,seconds,method):
        return WebDriverWait(self._driver, seconds).until(method=method)

