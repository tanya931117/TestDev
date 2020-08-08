#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/12 23:29
# @Author  : tanya
# @File    : conftest.py
# @Software: PyCharm
import os
import pytest
from pythoncode.my_utils.get_path import get_root_Path


@pytest.fixture()
def start_case():
    print("case开始....")
    yield print("case结束....")

#命令行添加参数
def pytest_addoption(parser):
    group = parser.getgroup("my_args_group")
    group.addoption(
        "--env",
        action="store",
        dest="env",
        default="test",
        help="将命令行参数 '--env' 添加到 pytest 配置中"
    )

root_path = get_root_Path()
path = os.path.join(root_path, "my_yaml")

def pytest_generate_tests(metafunc):
    #若方法参数包含start_case，则加载参数
    if ("start_case" in metafunc.fixturenames):
        #获取命令行参数env的值，默认为test
        enviroment = metafunc.config.getoption("env")
        try:
            #从类变量func_params中获取方法对应的参数化文件及参数名称
            #例：func_params = {"test_all": ["name,userid,mobile,department", "add_member_api.yml"]}
            param = metafunc.cls.func_params[metafunc.function.__name__]
            # @pytest.mark.parametrize("value1,value2,check",get_params(os.path.join(path,"add_case.yml")))
            # tmp = metafunc.cls.get_params(os.path.join(path, enviroment, param[1]))
            #根据不同的env，获取不同路径下的yml文件，为方法进行参数化
            metafunc.parametrize(param[0], metafunc.cls.get_params(os.path.join(path,enviroment,param[1])))
        except:
            #若发生异常，不做任何参数化
            pass
    else:
        #若方法采纳数中不包含start_case，则不做参数化
        pass