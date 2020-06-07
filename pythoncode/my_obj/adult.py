#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/7 16:16
# @Author  : tanya
# @File    : adult.py
# @Software: PyCharm
from pythoncode.my_obj.person import person

class adult(person):
    def __init__(self,name,age,high,weight,work):
        super(adult, self).__init__(name,age,high,weight)
        self.work=work

    def go_to_work(self,work):
        print(f"my work is {self.work},i should {work}")

    def info(self):
        super(adult, self).info()
        print(f"my work is {self.work}")