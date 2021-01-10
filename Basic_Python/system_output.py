# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-04 19:09:36
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-04 21:09:33
# @Title: Program to get system command output

import os

cmd = "git --version"

returned_value = os.system(cmd)  # returns the exit code in unix
print('returned value:', returned_value) #we are not printing the git version command output to console, it’s being printed because console is the standard output stream here

       # import subprocess
       # cmd = "git --version"
       # returned_value = subprocess.call(cmd, shell=True)  # returns the exit code in unix
       # print('returned value:', returned_value)
