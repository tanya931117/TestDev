# -*- coding: utf-8 -*-
# @Time    : 2020-6-9 13:41
# @Author  : tanya
# @Email   : tan.li@51job.com
# @File    : test_baidu.py
# @Software: PyCharm
# @Desciption: selenium+pytest+allure
import os

import allure
import pytest
import yaml
from selenium import webdriver
import time
##跳过整个模块的测试
# pytest.skip("skipping module TestBaidu", allow_module_level=True)

#跳过整个模块的测试
# pytestmark = pytest.mark.skipif(True, reason="skipif all Class")

#模块间共享有条件的跳过
# markskipif = pytest.mark.skipif(True, reason="share ski in module")

#整个类的测试都跳过
# @pytest.mark.skipif(True, reason="skipif TestBaidu")
@allure.feature("百度")
class TestBaidu():

    def setup_class(self):
        print("setup_class")
    def teardown_class(self):
        print("teardown_class")
    def setup_method(self):
        print("setup_method")
    def teardown_method(self):
        print("teardown_method")

    @pytest.fixture()
    def my_fixture(self):
        print("my_fixture")

    @allure.story("搜索")
    @pytest.mark.parametrize("kws",yaml.safe_load(open("./my_yaml/baidu_yaml.yml","r")))
    def test_search(self,kws,my_fixture):
        with allure.step("打开浏览器"):
            browser = webdriver.Chrome("D:\\chromedriver.exe")
            browser.maximize_window()
        with allure.step("访问百度"):
            browser.get("https://www.baidu.com")
        with allure.step(f"输入关键字：{kws}"):
            search_input_element = browser.find_element_by_id("kw")
            search_input_element.send_keys(kws)
        with allure.step("点击搜索"):
            search_element = browser.find_element_by_id("su")
            search_element.click()
        time.sleep(5)
        file_path = f"../image/test_search_{kws}.png"
        browser.save_screenshot(file_path)
        allure.attach.file(source=file_path, name="screentshot", attachment_type=allure.attachment_type.PNG)
        browser.quit()

    # @pytest.mark.skip(reason="i just want to skip")
    # @pytest.mark.parametrize("kws", yaml.safe_load(open("pythoncode\\baidu_yaml.yml", "r")))
    # def test_search2(self, kws, my_fixture):
    #     # pytest.skip("i just want to skip")
    #     browser = webdriver.Chrome("D:\\chromedriver_win32\\chromedriver.exe")
    #     browser.get("https://www.baidu.com")
    #     search_input_element = browser.find_element_by_id("kw")
    #     search_input_element.send_keys(kws)
    #     search_element = browser.find_element_by_id("su")
    #     search_element.click()
    #     time.sleep(5)
    #     browser.quit()

    # @pytest.mark.skipif(True, reason="skipif")
    # @markskipif
    # @pytest.mark.parametrize("kws", yaml.safe_load(open("pythoncode\\baidu_yaml.yml", "r")))
    # def test_search3(self, kws, my_fixture):
    #     pytest.skip("i just want to skip")
    #     browser = webdriver.Chrome("D:\\chromedriver_win32\\chromedriver.exe")
    #     browser.get("https://www.baidu.com")
    #     search_input_element = browser.find_element_by_id("kw")
    #     search_input_element.send_keys(kws)
    #     search_element = browser.find_element_by_id("su")
    #     search_element.click()
    #     time.sleep(5)
    #     browser.quit()

# class TestBaidu1():
#     @pytest.mark.parametrize("kws",yaml.safe_load(open("pythoncode\\baidu_yaml.yml","r")))
#     def test_search(self,kws):
#         browser = webdriver.Chrome("D:\\chromedriver_win32\\chromedriver.exe")
#         browser.get("https://www.baidu.com")
#         search_input_element = browser.find_element_by_id("kw")
#         search_input_element.send_keys(kws)
#         search_element = browser.find_element_by_id("su")
#         search_element.click()
#         time.sleep(5)
#         browser.quit()
