#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/8 10:34
# @Author  : tanya
# @File    : contact_member_api.py
# @Software: PyCharm
from pythoncode.PO.base_api import BaseApi


class ContactMemberApi(BaseApi):
    _contact_secret = "K_s1vBSMulzcOe_r3P1CB7JvqZ_QWUUpQ6kwbJaia_U"
    def add_member(self,params,token):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/create",
            "params":{
                "access_token":token
            },
            "json": params
        }
        return self.send_request(**data)

    def update_member(self,params,token):
        data = {
            "method":"post",
            "url":"https://qyapi.weixin.qq.com/cgi-bin/user/update",
            "params": {
                "access_token": token
            },
            "json":params
        }
        return self.send_request(**data)

    def get_member(self,params,token):
        params["access_token"] = token
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/get",
            "params": params
        }
        return self.send_request(**data)

    def del_member(self,params,token):
        params["access_token"] = token
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/delete",
            "params": params
        }
        return self.send_request(**data)
