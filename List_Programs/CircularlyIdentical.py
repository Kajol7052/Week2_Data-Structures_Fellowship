# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-08 22:57:49
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-08 23:36:21
# @Title: Program to check whether two lists are circularly identical.
class IdenticalList:
    def __init__(self,my_list1,my_list2):
        self.my_list1 = my_list1
        self.my_list2 = my_list2
        
    def circular_identical(self):
        my_list3 = self.my_list1 * 2
        for x in range(0, len(self.my_list1)):
            z = 0
            for y in range(x, x + len(self.my_list1)):
                if my_list2[z]== my_list3[y]:
                    z+= 1
                else:
                    break
            if z == len(my_list1):
                return True
        return False

my_list1 = [1, 2, 1, 1, 3]
my_list2 = [3, 1, 2, 1, 1]
identicalList = IdenticalList(my_list1,my_list2)
print(identicalList.circular_identical())
