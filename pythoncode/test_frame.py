#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/20 17:25
# @Author  : tanya
# @File    : test_frame.py
# @Software: PyCharm
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class TestFrame():
    def setup(self):
        self.driver = webdriver.Chrome("D:\\workspace\\pyworkspace\\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://www.w3cschool.cn/tryrun/showhtml/tryhtml5_draganddrop")
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_frame(self):
        iframe = self.driver.find_element(By.ID,"result-iframe")
        self.driver.switch_to.frame(iframe)
        p = self.driver.find_element(By.CSS_SELECTOR,"body > p")
        print(p.text)
        div1 = self.driver.find_element(By.ID,"div1")
        drag1 = self.driver.find_element(By.ID, "drag1")
        draggable = drag1.get_attribute("draggable")
        print(f"is draggable:{draggable}")
        actions = ActionChains(self.driver)
        actions.drag_and_drop(drag1,div1).pause(3)
        actions.perform()
        print("drag......")
        self.driver.switch_to.parent_frame()
        self.driver.execute_script("alert('alert')")
        alert = self.driver.switch_to.alert
        print(alert.text)
        alert.accept()
        time.sleep(10)

