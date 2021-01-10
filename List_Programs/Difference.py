# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-06 19:57:01
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-08 00:25:51
# @Title: Program to get the difference between the two lists 
 
class DifferenceLists:

    def __init__(self,list1,list2):
        self.list1 = list1
        self.list2 = list2

    def difference_of_two_lists(self):
        list_diff = [i for i in self.list1+self.list2 if (i not in self.list1 or i not in self.list2)]
        return list_diff

 
if __name__ == "__main__":
    list1 = [10, 15, 20, 25, 30, 35, 40]
    list2 = [25, 40, 35]
    ListDifference = DifferenceLists(list1,list2)
    list3 = ListDifference.difference_of_two_lists()
    print(list3)

