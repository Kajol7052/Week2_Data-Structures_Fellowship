# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-05 20:49:17
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-06 10:40:56
# @Title: Program to find maximum and the minimum value in a set
class MaxMin:
    def max_min(self,new_list):
        size = len(new_list)
        for i in range(size): # Bubble Sort
            for j in range(i+1,size-1):
                if new_list[j+1] < new_list[j]:
                    temp = new_list[j]
                    new_list[j] = new_list[j+1]
                    new_list[j+1] = temp
        return new_list


my_set = set()
size = int(input("Enter the size of the set: "))
for i in range(size):
    my_set.add(int(input("Enter the unique elements in set: ")))
print("Set is: ", my_set)
my_list = list(my_set)
maxMin = MaxMin()
my_list = maxMin.max_min(my_list)
print("Maximum element in set is: ",my_list[size-1]) # print the maximum element
print("Minimum element in set is: ",my_list[0]) # print the minimum element
print(maxMin.max_min.__doc__)