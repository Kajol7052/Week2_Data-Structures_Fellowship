# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-04 23:04:42
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-05 23:51:11
# @Title: Program to remove the first occurrence of a specified element from an array

class OccurRemoval:
    def removesFirstOcurrencesElement(self,arr, searchElement):
        '''
        Methode to remove the first occurrence 
        of a specified element from an array
        '''
        for index in range(size):
            if searchElement == arr[index]:
                arr.remove(arr[index])
                break


size=(int(input("Enter the size of array: ")))
arr=[]
for x in range(size):
    element=(int(input("Enter the value: ")))
    arr.append(element)    
number=(int(input("Enter number to remove the first ocurrence: ")))
occurRemoval = OccurRemoval()
occurRemoval.removesFirstOcurrencesElement(arr,number)
print("After removing the element: ")
newSize=len(arr)
for x in range(newSize):
    print(arr[x])
print(occurRemoval.removesFirstOcurrencesElement.__doc__)