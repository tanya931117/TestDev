#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/6 20:05
# @Author  : tanya
# @File    : base_api.py
# @Software: PyCharm
import requests


class BaseApi:
    def send_request(self, **req_data):
        return requests.request(**req_data)