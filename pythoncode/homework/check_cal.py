#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/12 23:24
# @Author  : tanya
# @File    : check_cal.py
# @Software: PyCharm
import os

import allure
import pytest
import yaml

from pythoncode.my_utils.calcutor import add,subtract,multiply,divide
from pythoncode.my_utils.get_path import get_root_Path

@pytest.mark.usefixtures("print_cal")
class CheckCal():
    func_params = {"check_add": ["value1,value2,check", "add_case.yml"],
                   "check_multiply": ["value1,value2,check", "multiply_case.yml"],
                   "check_subtract": ["value1,value2,check", "subtract_case.yml"],
                   "check_divide": ["value1,value2,check", "divide_case.yml"]}

    def get_params(path):
        with open(path,"r") as f:
            params = yaml.safe_load(f)
        res = []
        for param in params:
            values = param[:-2]
            dependency_name = param[-2]
            depend = param[-1]
            if depend :
                res.append(pytest.param(*values,marks=pytest.mark.dependency(name=dependency_name,depends=depend)))
            else:
                res.append(pytest.param(*values, marks=pytest.mark.dependency(name=dependency_name)))
        return res

    @pytest.mark.run(order=1)
    # @pytest.mark.parametrize("value1,value2,check",get_params(os.path.join(path,"add_case.yml")))
    def check_add(self,value1,value2,check):
        # print(f"value1:{value1},value2:{value2}")
        result = add(value1,value2)
        assert result==check

    @pytest.mark.run(order=3)
    # @pytest.mark.parametrize("value1,value2,check",get_params(os.path.join(path,"multiply_case.yml")))
    def check_multiply(self,value1,value2,check):
        result=multiply(value1,value2)
        assert result==check

    @pytest.mark.run(order=2)
    # @pytest.mark.parametrize("value1,value2,check",get_params(os.path.join(path,"subtract_case.yml")))
    def check_subtract(self,value1,value2,check):
        result = subtract(value1,value2)
        assert result==check

    @pytest.mark.run(order=4)
    # @pytest.mark.parametrize("value1,value2,check",get_params(os.path.join(path,"divide_case.yml")))
    def check_divide(self,value1,value2,check):
        result = divide(value1, value2)
        assert result == check