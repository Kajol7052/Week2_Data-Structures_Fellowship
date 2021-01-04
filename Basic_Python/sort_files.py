# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-04 19:09:22
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-04 20:55:54
# @Title: Program to sort files by date

from glob import glob # glob module is used to retrieve files/pathnames matching a specified pattern.
import os

files = glob("*.py")
files.sort(key=os.path.getmtime)
print("\n".join(files))