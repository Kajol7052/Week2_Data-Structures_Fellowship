# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-04 23:05:18
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-05 23:54:05
# @Title: Program to get the number of occurrences of a specified element in an array
class MultipleOccurence:
    def ocurrencesOfElement(self,array,searchElement):
        '''
        Method to get the number of occurrences 
        of a specified element in an array
        '''
        count = 0
        for x in range(size):
            print(arr[x])
            if searchElement == array[x]:
                count+=1
        return count

size=(int(input("Enter the size of array: ")))
arr=[]
for x in range(size):
    element=(int(input("Enter the value: ")))
    arr.append(element)
number = (int(input("Enter number to be find the ocurrences: ")))
multipleOccurence  = MultipleOccurence()
print("No of ocurrences of",number,"is",multipleOccurence.ocurrencesOfElement(arr,number))
print(multipleOccurence.ocurrencesOfElement.__doc__)