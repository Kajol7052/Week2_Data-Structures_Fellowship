# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-04 19:08:54
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-04 20:57:50
# @Title: Program to get the command-line arguments (name of the script, the number of arguments, arguments) passed to a script. 

#   It means your importing OS module in Python which provides a way of using 
#   operating system dependent functionality. 
import sys

print("This is the name/path of the script %s " % sys.argv[0])
print("Number of arguments:",len(sys.argv))
print("Argument List:",str(sys.argv))