# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-04 19:07:04
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-04 20:09:26
# @Title: Program to check whether a file exists

#   The os.path module is always the path module suitable for the operating system 
#   Python is running on, and therefore usable for local paths. However, you can also 
#   import and use the individual modules if you want to manipulate a path that is always 
#   in one of the different formats.

import os.path

# function to check whether file exists or not
def file_exist_or_not():
    open('abc.txt', 'w')
    print(os.path.isfile('abc.txt'))
    print(os.path.isfile('xyz.txt'))

file_exist_or_not()