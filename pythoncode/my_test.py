#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/12 22:49
# @Author  : tanya
# @File    : my_test.py
# @Software: PyCharm
import time

import allure
import pytest
import yaml
from selenium import webdriver

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

if __name__=="__main__":
    # pytest.param(1, 2, marks=pytest.mark.dependency(name="b1", depends=["a1", "a2"]))
    file_path = "/pythoncode/my_yaml/test/subtract_case.yml"
    print(get_params(file_path))