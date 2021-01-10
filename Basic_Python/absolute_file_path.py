# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-04 18:57:53
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-04 20:49:15
# @Title: Program to get an absolute file path

import os

def absolute_file_path(path_name):
        return os.path.abspath('path_name')        
print("Absolute file path: ",absolute_file_path("reverse_username.py"))
