#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/13 0:13
# @Author  : tanya
# @File    : get_path.py
# @Software: PyCharm
import os


def get_root_Path():
    path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    return path