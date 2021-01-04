# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-04 19:07:10
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-04 20:02:06
# @Title: Create a histogram from a given list of integers

# function to create histogram from list of integers
def histogram_from_integers(lists):
    for num in lists:
        result = ''
        iteration = num
        while iteration > 0:
          result += '*'
          iteration = iteration - 1
        print(result)
    print()

histogram_from_integers([1,2,3,4])
histogram_from_integers([5,4,3,2,1])