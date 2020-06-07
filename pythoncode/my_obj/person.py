#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/7 16:04
# @Author  : tanya
# @File    : person.py
# @Software: PyCharm

high = 170
weight = 60
name = ""
age = 18

class person():
    def __init__(self,name,age,high,weight):
        self.name=name
        self.age=age
        self.high=high
        self.weight=weight

    def eat(self,food):
        print(f"eat a {food}")

    def drink(self,drink):
        print(f"drink {drink}")

    def walk(self):
        print("walk")

    def info(self):
        print(f"my name is {self.name}")
        print(f"my age is {self.age}")
        print(f"my high is {self.high}")
        print(f"my weight is {self.weight}")