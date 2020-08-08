#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/8 10:45
# @Author  : tanya
# @File    : we_work_api.py
# @Software: PyCharm
import json
import os
import time

from pythoncode.PO.base_api import BaseApi
from pythoncode.my_utils import get_path


class WeWorkApi(BaseApi):
    root_path = get_path.get_root_Path()
    def access_token(self,secret):
        ##通讯录管理-"K_s1vBSMulzcOe_r3P1CB7JvqZ_QWUUpQ6kwbJaia_U"
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        corpid = "ww0c8f13621be7beef"
        data = {
            "method":"get",
            "url": url,
            "params": {
                "corpid": corpid,
                "corpsecret": secret
            }
        }
        token = None
        # response = requests.get(url=url, params=data)
        response = self.send_request(**data)
        file = os.path.join(self.root_path, "contact_tocken.txt")
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

    def get_token(self,secret):
        token = None
        ##从文件里获取token
        is_exist = os.path.exists(os.path.join(self.root_path,"contact_tocken.txt"))
        if is_exist:
            file_size = os.path.getsize(os.path.join(self.root_path,"contact_tocken.txt"))
            if file_size>0:
                with open(os.path.join(self.root_path,"contact_tocken.txt"),"r",encoding="utf-8") as f:
                    token_data = json.load(f)
                    ##判断token是否过期
                    expires_date = token_data["expires_date"]
                    if expires_date<time.time():##token已过期，需重新获取
                        token = self.access_token(secret)
                    else:##token未过期，可直接使用
                        token = token_data["access_token"]
            else:##文件为空，调用接口获取token，并且写入文件
                token = self.access_token(secret)
        ##文件不存在，调用接口获取token，并且写入文件
        else:
            token = self.access_token(secret)
        return token