#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/8 13:27
# @Author  : tanya
# @File    : test_tag_manage.py
# @Software: PyCharm
import pytest
import yaml

from pythoncode.PO.contact_tag_api import ContactTagApi
from pythoncode.PO.we_work_api import WeWorkApi


@pytest.mark.usefixtures("start_case")
class TestTagManage():

    def setup_class(self):
        self.contact_tag = ContactTagApi()
        wework =WeWorkApi()
        self.token = wework.get_token(self.contact_tag._contact_secret)

    #用钩子函数pytest_generate_tests加载参数
    func_params = {"test_all": ["tagname", "add_tag_api.yml"],
                   "test_tag_mem":["tagid,userlist","add_tag_mem_api.yml"]}
    def get_params(path):
        with open(path, "r",encoding="utf-8") as f:
            params = yaml.safe_load(f)
        return params

    @pytest.mark.skip
    def test_all(self,tagname):
        response = self.contact_tag.get_tag_list(self.token)
        result = response.json()
        #{'errcode': 0, 'errmsg': 'ok', 'taglist': [{'tagid': 1, 'tagname': '标签一'}, {'tagid': 2, 'tagname': '标签二'}]}
        if len(result["taglist"]) >0:
            for tag in result["taglist"]:
                if tag["tagname"] == tagname:
                    self.contact_tag.del_tag({"tagid":tag["tagid"]},self.token)
                    break
        tag = {
            "tagname": tagname
        }
        res = self.contact_tag.add_tag(tag,self.token)
        assert res.json()["errmsg"].startswith("created")

    def test_tag_mem(self,tagid,userlist):
        response = self.contact_tag.get_tag_mems({"tagid":tagid},self.token)
        result = response.json()
        #{'errcode': 0, 'errmsg': 'ok', 'userlist': [{'userid': 'LiTan', 'name': '李土云'}, {'userid': 'Miao', 'name': '张世锋'}, {'userid': 'eunhyuk.lee', 'name': 'LeeEunHyuk'}, {'userid': 'donghae.lee', 'name': 'LeeDongHae'}], 'partylist': [], 'tagname': '标签一'}
        if len(result["userlist"]) > 0:
            userlist_del = []
            for user in result["userlist"]:
                if user["userid"] in userlist:
                    userlist_del.append(user["userid"])
            if len(userlist_del) > 0 :
                params = {
                    "tagid": tagid,
                    "userlist": userlist_del
                }
                self.contact_tag.del_tag_mem(params,self.token)
        params = {
            "tagid": tagid,
            "userlist": userlist
        }
        res = self.contact_tag.add_tag_mem(params,self.token).json()
        #{'errcode': 0, 'errmsg': 'ok', 'invalidparty': []}
        assert res["errmsg"] == "ok"

