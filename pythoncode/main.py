#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/7 16:26
# @Author  : tanya
# @File    : main.py
# @Software: PyCharm
from pythoncode.my_obj.adult import adult
from pythoncode.my_obj.children import children
import yaml
import os

# a = adult("tanya",26,170,62,"tester")
# c = children("donghae",16,170,110)
# print("------a 自我介绍")
# a.info()
# a.work("test a software")
# print("------c 自我介绍")
# c.go_to_school("junior")
# c.info()
# print("------eat")

path = os.path.join(os.path.abspath("."), "my_yaml")

with open(os.path.join(path,"xiaohai.yaml"),"r") as f:
    xiaohai = yaml.load(f,Loader=yaml.Loader)
    a = adult(xiaohai["name"],xiaohai["age"],xiaohai["high"],xiaohai["weight"],xiaohai["work"])
    print("------xiaohai自我介绍")
    a.info()
    a.go_to_work(xiaohai["works"][0])

with open(os.path.join(path, "xiaoming.yaml"), "r") as f:
    xiaoming = yaml.load(f, Loader=yaml.Loader)
    c = children(xiaoming["name"],xiaoming["age"],xiaoming["high"],xiaoming["weight"])
    print("------xiaoming自我介绍")
    c.go_to_school("junior")
    c.info()
    c.go_to_class(xiaoming["course"][0])
