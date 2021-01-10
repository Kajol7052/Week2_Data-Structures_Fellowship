# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-04 19:06:22
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-04 20:16:59
# @Title: Program to call an external command in Python


#from subprocess import call
#call(["ls", "-l"])

#   Subprocess module for running external programs 
#   and reading their outputs in your Python code.
import subprocess
#   The subprocess.run method takes a list of arguments. When the 
#   method is called, it executes the command and waits for the process 
#   to finish, returning a “CompletedProcess” object in the end.
subprocess.run(["ls", "-l"])