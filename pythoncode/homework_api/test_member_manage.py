#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/8 10:43
# @Author  : tanya
# @File    : test_member_manage.py
# @Software: PyCharm
import pytest
import yaml

from pythoncode.PO.contact_member_api import ContactMemberApi
from pythoncode.PO.we_work_api import WeWorkApi

@pytest.mark.usefixtures("start_case")
class TestMember():
    def setup_class(self):
        self.contact_mem = ContactMemberApi()
        wework =WeWorkApi()
        self.token = wework.get_token(self.contact_mem._contact_secret)

    def create_data(self):
        return [("BM"+str(x),"matthew"+str(x),"137%08d"%x) for x in range(20)]

    #用钩子函数pytest_generate_tests加载参数
    func_params = {"test_all": ["name,userid,mobile,department", "add_member_api.yml"]}
    def get_params(path):
        with open(path, "r",encoding="utf-8") as f:
            params = yaml.safe_load(f)
        return params

    def test_all(self,name,userid,mobile,department):
        response = self.contact_mem.get_member({"userid":userid},self.token)
        result = response.json()
        if result["errcode"] == 0:
            self.contact_mem.del_member({"userid":userid},self.token)
        member = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        res = self.contact_mem.add_member(member, self.token).json()
        assert res["errmsg"].startswith("created")
