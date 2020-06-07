#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/7 16:21
# @Author  : tanya
# @File    : children.py
# @Software: PyCharm
from pythoncode.my_obj.person import person


class children(person):
    def __init__(self,name,age,high,weight):
        super(children, self).__init__(name,age,high,weight)
        self.school =""

    def go_to_school(self,school):
        self.school=school
        print(f"i will go to school, {school}")

    def go_to_class(self,course):
        print(f"i should go to {course}")

    def info(self):
        super(children, self).info()
        print(f"my school is {self.school}")