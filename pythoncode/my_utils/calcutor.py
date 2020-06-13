#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/12 23:49
# @Author  : tanya
# @File    : calcutor.py
# @Software: PyCharm

def add(x, y):
    """相加"""
    return x + y

def subtract(x, y):
    """相减"""
    return x - y

def multiply(x, y):
    """相乘"""
    return x * y

def divide(x, y):
    """相除"""
    if y==0:
        return "Divisor cannot be 0"
    else:
        return x / y