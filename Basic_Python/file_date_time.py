# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-04 19:06:58
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-04 20:51:30
# @Title: Program to get file creation and modification date/times

import os
import datetime
 
file = "histogram.py"
 
print("Created")
print(os.path.getctime(file))
print(datetime.datetime.fromtimestamp(os.path.getctime(file)))
 
print()
 
print("Modified")
print(os.path.getmtime(file))
print(datetime.datetime.fromtimestamp(os.path.getmtime(file)))