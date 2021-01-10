# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-05 19:04:11
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-05 19:05:35
# @Title: Program to count the values associated with key in a dictionary

# data given in ques
student = [{'id': 1, 'success': True, 'name': 'Lary'},{'id': 2, 'success': False, 'name': 'Rabi'},{'id': 3, 'success': True, 'name': 'Alex'}]

count=0
for x in student:
    if x['success'] == True:
        count+=1
print("Count of true: ",count)