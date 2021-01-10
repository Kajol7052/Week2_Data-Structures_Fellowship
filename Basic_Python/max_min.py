# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-04 19:07:41
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-04 21:29:40
# @Title: Function to find the maximum and minimum numbers from a sequence of numbers. 


# function to return max and min from list
def max_min(data):
  maximum = data[0]
  minimum = data[0]
  for num in data:
    if num > maximum:
      maximum = num
    elif num < minimum:
        minimum = num
  return maximum, minimum

print(max_min([0, 10, 15, 40, -5, 42, 17, 28, 75]))