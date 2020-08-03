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
    if ("start_case" in metafunc.fixturenames):
        enviroment = metafunc.config.getoption("env")
        try:
            param = metafunc.cls.func_params[metafunc.function.__name__]
            # @pytest.mark.parametrize("value1,value2,check",get_params(os.path.join(path,"add_case.yml")))
            # tmp = metafunc.cls.get_params(os.path.join(path, enviroment, param[1]))
            metafunc.parametrize(param[0], metafunc.cls.get_params(os.path.join(path,enviroment,param[1])))
        except:
            pass
    else:
        pass