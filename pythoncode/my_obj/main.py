#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/7 16:26
# @Author  : tanya
# @File    : main.py
# @Software: PyCharm
from pythoncode.my_obj.adult import adult
from pythoncode.my_obj.children import children

a = adult("tanya",26,170,62,"tester")
c = children("donghae",16,170,110)
print("------a 自我介绍")
a.info()
print("------c 自我介绍")
c.go_to_school("junior")
c.info()
print("------eat")
a.eat("汉堡包")
c.eat("三明治")
print("类变量与实例变量")
print("a.age="+str(a.age))
