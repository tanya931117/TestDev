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
    func_params = {"test_add": ["value1,value2,check,dependency_name,depends", "add_case.yml"],
                   "test_multiply": ["value1,value2,check,dependency_name,depends", "multiply_case.yml"],
                   "test_subtract": ["value1,value2,check,dependency_name,depends", "subtract_case.yml"],
                   "test_divide": ["value1,value2,check,dependency_name,depends", "divide_case.yml"]}
    def get_params(path):
        with open(path, "r") as f:
            params = yaml.safe_load(f)
        return params

    @allure.story("测试加法")
    # @pytest.mark.parametrize("value1,value2,check,dependency_name,depends",yaml.safe_load(open(os.path.join(path,"add_case.yml"),"r")))
    def test_add(self,value1,value2,check,dependency_name,depends):
        # print(f"value1:{value1},value2:{value2}")
        result = add(value1,value2)
        assert result==check

    @allure.story("测试减法")
    # @pytest.mark.parametrize("value1,value2,check,dependency_name,depends",yaml.safe_load(open(os.path.join(path,"subtract_case.yml"),"r")))
    def test_subtract(self,value1,value2,check,dependency_name,depends):
        result = subtract(value1,value2)
        assert result==check

    @allure.story("测试乘法")
    # @pytest.mark.parametrize("value1,value2,check,dependency_name,depends",yaml.safe_load(open(os.path.join(path,"multiply_case.yml"),"r")))
    def test_multiply(self,value1,value2,check,dependency_name,depends):
        result=multiply(value1,value2)
        assert result==check

    @allure.story("测试除法")
    # @pytest.mark.parametrize("value1,value2,check,dependency_name,depends",yaml.safe_load(open(os.path.join(path,"divide_case.yml"),"r")))
    def test_divide(self,value1,value2,check,dependency_name,depends):
        result=divide(value1,value2)
        assert result==check