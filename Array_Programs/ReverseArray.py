# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-04 23:06:44
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-05 23:53:08
# @Title: Program to reverse the order of the items in the array

class ArrayReversal:
    def reverseArray(self,array):
        '''
        Method to reverse the order of the items in the array
        '''
        x = len(array)
        while x >= 0:
            print(arr[x])
            x-=1

size=(int(input("Enter the size of array: ")))
arr = []
for x in range(size):
    element=(int(input("Enter the value: ")))
    arr.append(element)
arrayReversal = ArrayReversal() # object instantiated
print(arrayReversal.reverseArray.__doc__)
