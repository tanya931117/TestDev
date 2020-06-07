#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/7 15:19
# @Author  : tanya
# @File    : my_func.py
# @Software: PyCharm

def have_parameters(param1:str,param2:int):
    print(f"参数1为{param1}")
    print(f"参数2为{param2}")
    return param1

def no_parameters():
    print("该方法没有参数，且无返回值")

if __name__ == "__main__":
    have_parameters("lalala",123)
    no_parameters()