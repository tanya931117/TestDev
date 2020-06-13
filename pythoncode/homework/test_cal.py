#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/12 23:24
# @Author  : tanya
# @File    : test_cal.py
# @Software: PyCharm
import os

import allure
import pytest
import yaml

from pythoncode.my_utils.calcutor import add,subtract,multiply,divide
from pythoncode.my_utils.get_path import get_root_Path

root_path = get_root_Path()
path = os.path.join(root_path, "my_yaml")

@pytest.mark.usefixtures("print_cal")
@pytest.mark.calcutor
@allure.feature("测试计算器")
class TestCal():
    @allure.story("测试加法")
    @pytest.mark.parametrize("value1,value2,check",yaml.safe_load(open(os.path.join(path,"add_case.yml"),"r")))
    def test_add(self,value1,value2,check):
        # print(f"value1:{value1},value2:{value2}")
        result = add(value1,value2)
        assert result==check

    @allure.story("测试减法")
    @pytest.mark.parametrize("value1,value2,check",yaml.safe_load(open(os.path.join(path,"subtract_case.yml"),"r")))
    def test_subtract(self,value1,value2,check):
        result = subtract(value1,value2)
        assert result==check

    @allure.story("测试乘法")
    @pytest.mark.parametrize("value1,value2,check",yaml.safe_load(open(os.path.join(path,"multiply_case.yml"),"r")))
    def test_multiply(self,value1,value2,check):
        result=multiply(value1,value2)
        assert result==check

    @allure.story("测试除法")
    @pytest.mark.parametrize("value1,value2,check",yaml.safe_load(open(os.path.join(path,"divide_case.yml"),"r")))
    def test_divide(self,value1,value2,check):
        result=divide(value1,value2)
        assert result==check

