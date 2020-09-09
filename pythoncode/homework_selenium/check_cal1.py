#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/12 23:24
# @Author  : tanya
# @File    : check_cal1.py
# @Software: PyCharm
import os
import pytest
import yaml
from pythoncode.my_utils.calcutor import add,subtract,multiply,divide



@pytest.mark.usefixtures("print_cal")
class CheckCal():
    func_params = {"check_add": ["value1,value2,check,dependency_name,depends", "add_case.yml"],
                   "check_multiply": ["value1,value2,check,dependency_name,depends", "multiply_case.yml"],
                   "check_subtract": ["value1,value2,check,dependency_name,depends", "subtract_case.yml"],
                   "check_divide": ["value1,value2,check,dependency_name,depends", "divide_case.yml"]}

    def get_params(path):
        with open(path, "r") as f:
            params = yaml.safe_load(f)
        return params

    @pytest.mark.dependency(name="add")
    # @pytest.mark.parametrize("value1,value2,check,dependency_name,depends", get_params("add_case.yml"))
    def check_add(self,value1,value2,check,dependency_name,depends):
        result = add(value1, value2)
        assert False

    @pytest.mark.dependency(name="multiply")
    # @pytest.mark.parametrize("value1,value2,check,dependency_name,depends", get_params("multiply_case.yml"))
    def check_multiply(self,value1,value2,check,dependency_name,depends):
        result = multiply(value1, value2)
        assert False

    @pytest.mark.dependency(depends=["add"])
    # @pytest.mark.parametrize("value1,value2,check,dependency_name,depends", get_params("subtract_case.yml"))
    def check_subtract(self,value1,value2,check,dependency_name,depends):
        result = subtract(value1, value2)
        assert result==check

    @pytest.mark.dependency(depends=["multiply"])
    # @pytest.mark.parametrize("value1,value2,check,dependency_name,depends", get_params("divide_case.yml"))
    def check_divide(self,value1,value2,check,dependency_name,depends):
        result = divide(value1, value2)
        assert result == check

