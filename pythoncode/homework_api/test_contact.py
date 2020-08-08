#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/3 19:33
# @Author  : tanya
# @File    : test_contact.py
# @Software: PyCharm
import json
import os
import time

import pytest
import requests
import yaml

from pythoncode.my_utils import get_path

root_path = get_path.get_root_Path()

class TestContact:

    #企业ID：ww0c8f13621be7beef
    #通讯录管理secret：K_s1vBSMulzcOe_r3P1CB7JvqZ_QWUUpQ6kwbJaia_U

    def access_token(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        data = {
            "corpid": "ww0c8f13621be7beef",
            "corpsecret": "K_s1vBSMulzcOe_r3P1CB7JvqZ_QWUUpQ6kwbJaia_U"
        }
        token = None
        response = requests.get(url=url, params=data)
        file = os.path.join(root_path, "contact_tocken.txt")
        if response.status_code == 200:
            result = json.loads(response.content)
            if result["errcode"] == 0:
                token = result["access_token"]
                result["expires_date"] = time.time() + result["expires_in"]
                with open(file, "w", encoding="utf-8") as f:
                    json.dump(result, f)
            else:
                raise ValueError("access token error!")
        else:
            with open(file, "w", encoding="utf-8") as f:
                json.dump("", f)
        return token

    def get_token(self):
        token = None
        ##从文件里获取token
        is_exist = os.path.exists(os.path.join(root_path,"contact_tocken.txt"))
        if is_exist:
            file_size = os.path.getsize(os.path.join(root_path,"contact_tocken.txt"))
            if file_size>0:
                with open(os.path.join(root_path,"contact_tocken.txt"),"r",encoding="utf-8") as f:
                    token_data = json.load(f)
                    ##判断token是否过期
                    expires_date = token_data["expires_date"]
                    if expires_date<time.time():##token已过期，需重新获取
                        token = self.access_token()
                    else:##token未过期，可直接使用
                        token = token_data["access_token"]
            else:##文件为空，调用接口获取token，并且写入文件
                token = self.access_token()
        ##文件不存在，调用接口获取token，并且写入文件
        else:
            token = self.access_token()
        return token

    def setup_method(self):
        data = {
            "access_token":self.get_token()
        }
        self.session = requests.Session()
        self.session.params=data

    @pytest.mark.skip
    def test_get_member(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/get"
        data = {
            "userid":"eunhyuk.lee"
        }
        response = self.session.get(url=url,params=data)
        print(response.status_code)
        print(response.content)

    @pytest.mark.skip
    def test_update_member(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/update"
        post = {
            "userid": "LiTan",
            "name": "李土云",
        }
        response = self.session.post(url=url,json=post)
        print(response.status_code)
        print(response.content)

    @pytest.mark.skip
    def test_add_member(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/create"
        post = {
            "userid": "eunhyuk.lee",
            "name": "LeeEunHyuk",
            "mobile": "13611111111",
            "department": [1]
        }
        response = self.session.post(url=url,json=post)
        print(response.status_code)
        print(response.content)

    @pytest.mark.skip
    def test_del_member(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/delete"
        data = {
            "userid": "eunhyuk.lee"
        }
        response = self.session.get(url=url,params=data)
        print(response.status_code)
        print(response.content)



