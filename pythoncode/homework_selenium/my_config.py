#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/14 14:15
# @Author  : tanya
# @File    : my_config.py.py
# @Software: PyCharm


class MyConfig():
    def __init__(self):
        self.env=""

    def get_env(self):
        return self.env

    def set_env(self,env):
        self.env=env

conf = MyConfig()


