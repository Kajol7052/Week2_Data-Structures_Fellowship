# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-04 19:05:31
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-04 20:40:45
# @Title: Program to access environment variables


import os

# Access all environment variables 
print('*----------------------------------*')
print(os.environ)
print('*----------------------------------*')
# Access a particular environment variable 
print(os.environ['HOME'])
print('*----------------------------------*')
print(os.environ['PATH'])
print('*----------------------------------*')