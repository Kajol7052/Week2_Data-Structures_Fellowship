# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-04 19:09:14
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-04 21:24:30
# @Title: Program to find files and skip directories of a given directory

import os
print([f for f in os.listdir('/Users/kajol7052/Desktop/Python_Basics/') if os.path.isfile(os.path.join('/Users/kajol7052/Desktop/Python_Basics/', f))])
