#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/12 23:29
# @Author  : tanya
# @File    : conftest.py
# @Software: PyCharm
import pytest

@pytest.fixture()
def print_cal():
    print("开始计算")
    yield print("计算结束")