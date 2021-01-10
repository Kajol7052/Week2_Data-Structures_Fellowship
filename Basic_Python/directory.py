# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-04 19:04:59
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-04 20:39:40
# @Title: Program to list all files in a directory in Python

from os import listdir
from os.path import isfile, join
files_list = [f for f in listdir('/Users/kajol7052/Desktop/Python_Basics') if isfile(join('/Users/kajol7052/Desktop/Python_Basics', f))]
print(files_list)
