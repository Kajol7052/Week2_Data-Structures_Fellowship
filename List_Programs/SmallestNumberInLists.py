# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-06 11:45:21
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-08 09:53:10
# @Title: Program to get the smallest number from a list

class SmallElement:

    def __init__(self,size):
        self.size = size

    def smallest_element_in_lists(self):
        for i in range(self.size):
            try:
                my_list.append(int(input("Enter the integer value in list: ")))
            except ValueError:
                print("Enter only integer values")
                continue
        print("Lists is: ", my_list)
        lists = min(my_list)
        print("Smallest element is: ", lists)

if __name__ == "__main__":
    my_list=[]
    size = int(input("Enter the size of lists: ")) 
    SmallItem = SmallElement(size)
    SmallItem.smallest_element_in_lists()
    