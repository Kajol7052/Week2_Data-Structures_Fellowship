# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-04 19:09:56
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-04 21:38:56
# @Title: Program to access and print a URL's content to the console

from http.client import HTTPConnection

conn = HTTPConnection("google.com")
conn.request("GET", "/")  
result = conn.getresponse()
# retrieves the entire contents
contents = result.read() 
print(contents)
