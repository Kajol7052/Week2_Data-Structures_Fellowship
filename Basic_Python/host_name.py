# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-04 19:07:16
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-04 21:08:43
# @Title: Program to get the name of the host on which the routine is running

#   The socket() function returns a socket object 
#   whose methods implement the various socket system calls.
import socket

host_name = socket.gethostname()
print()
print("Host name:", host_name)
print()
