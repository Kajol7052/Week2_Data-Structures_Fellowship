# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-06 19:18:11
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-08 10:10:58
# @Title: Program that takes two lists and returns True if they have at least one common member

class Intersection:

    def __init__(self):
        pass

    def intersection_of_lists(self,list1,list2):
        """
        function returns true if two list have atleast one common members
        list1: list 1
        list2: list 2
        return: return true or false
        """
        result=False
        for x in list1:
            for y in list2:
                if x == y: 
                    break
        return result

    def create_list(self,lists):
        size = int(input("Enter the size of list: "))
        lists = []
        for i in range(size):
            lists.append(input("Enter the value in lists: "))
        return lists
    


if __name__ == "__main__":
    my_list1 = my_list2 = []
    CommonMembers = Intersection()
    my_list1 = list(CommonMembers.create_list(my_list1))
    my_list2 = list(CommonMembers.create_list(my_list2))
    print("Common member present in List: ", CommonMembers.intersection_of_lists(my_list1,my_list2))

    

    