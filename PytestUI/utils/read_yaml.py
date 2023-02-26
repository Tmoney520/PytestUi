# -*- coding: utf-8 -*- 
"""          
# @Time   : 2023/2/25 19:01
#  :TGW
"""
import yaml


def yaml_data(file):
    with open(file,encoding="utf-8") as f:
        data = yaml.load(f,yaml.FullLoader)
    return data

