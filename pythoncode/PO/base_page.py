#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/20 18:22
# @Author  : tanya
# @File    : base_page.py
# @Software: PyCharm
import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
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
        """
        初始化PO的driver
        :param driver:
        """
        self._driver = None
        #若传入的driver为空，则初始化一个driver
        if driver is None:
            self._driver = webdriver.Chrome("D:\\workspace\\pyworkspace\\chromedriver.exe")
        #否则使用传入的driver
        else:
            self._driver = driver
        #若driver和访问的url均不为空，则访问url
        if self._base_url != "" and self._driver is not None:
            self._driver.get(self._base_url)
        #隐式等待1秒
        self._driver.implicitly_wait(1)

    def find(self,by,locator):
        """
        查找符合条件的第一个元素
        :param by:
        :param locator:
        :return:
        """
        return self._driver.find_element(by,locator)

    def finds(self,by,locator):
        """
        查找符合条件的所有元素
        :param by:
        :param locator:
        :return:
        """
        return self._driver.find_elements(by,locator)

    def add_cookie(self,cookies):
        """
        向浏览器中写cookie
        :param cookie_file:.json文件，文件中为cookie
        :return:None
        """
        with open(cookies, "r") as f:
            cookies = json.load(f)
        for cookie in cookies:
            self._driver.add_cookie(cookie)

    def execute_js(self,js,*args):
        """
        执行js
        :param js:js
        :param args:js参数
        :return:
        """
        self._driver.execute_script(js,*args)

    def get_cookie(self,cookie_file):
        """
        获取浏览器中写cookie
        :param cookie_file:cookie写入目的文件
        :return:None
        """
        cookies = self._driver.get_cookies()
        with open(cookie_file, "w") as f:
            json.dump(cookies, f)

    def refresh(self):
        #刷新页面
        self._driver.refresh()



    def wait_default(self,seconds,method:str,by,locator):
        """
        使用expected_conditions提供的内置方法
        :param seconds: 等待秒数
        :param method: clickable-等待元素可点击，visibility-等待元素课件，presence-等待元素在dom中出现
        :param by:元素定位方式，BasePage.css_selector......
        :param locator:元素定位路径
        :return:返回查找到的元素
        """
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
        """
        使用自定义等待函数
        :param seconds:等待秒数
        :param method:自定义的方法
        :return:返回查找到的元素
        """
        return WebDriverWait(self._driver, seconds).until(method=method)

