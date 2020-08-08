#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/8 13:11
# @Author  : tanya
# @File    : contact_tag_api.py
# @Software: PyCharm
from pythoncode.PO.base_api import BaseApi


class ContactTagApi(BaseApi):
    _contact_secret = "K_s1vBSMulzcOe_r3P1CB7JvqZ_QWUUpQ6kwbJaia_U"

    def add_tag(self,params,token):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/create",
            "params": {
                "access_token": token
            },
            "json": params
        }
        return self.send_request(**data)

    def del_tag(self,params,token):
        params["access_token"] = token
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/delete",
            "params": params,
        }
        return self.send_request(**data)

    def update_tag(self,params,token):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/update",
            "params": {
                "access_token": token
            },
            "json": params
        }
        return self.send_request(**data)

    def get_tag_list(self,token):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/list",
            "params": {
                "access_token": token
            },
        }
        return self.send_request(**data)

    def get_tag_mems(self,params,token):
        params["access_token"] = token
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/get",
            "params":params,
        }
        return self.send_request(**data)

    def add_tag_mem(self,params,token):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/addtagusers",
            "params": {
                "access_token": token
            },
            "json": params
        }
        return self.send_request(**data)

    def del_tag_mem(self,params,token):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/deltagusers",
            "params": {
                "access_token": token
            },
            "json": params
        }
        return self.send_request(**data)
