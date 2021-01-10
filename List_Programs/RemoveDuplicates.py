# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-06 18:16:29
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-08 10:00:23
# @Title: Program to remove duplicates from a list

class RemoveDuplicates:
    
    def __init__(self):
        size = int(input("Enter the size of list: ")) #stores the size of list
        my_list = [] #created empty lists
        #for loop to add element in list , loops until it reaches the size
        for i in range(size):
            my_list.append(input("Enter the value in list: "))
        print("Before removing duplicate values: ",my_list)
        self.my_list = my_list

    def remove_duplicates(self):
        """
        this function add unique element in one more list
        
        """
        unique_list=[]
        for item in self.my_list:
            if item not in unique_list:
                unique_list.append(item)
        return unique_list

if __name__ == "__main__":
    DuplicatesRemove = RemoveDuplicates()
    print("After removing duplicate values: ", DuplicatesRemove.remove_duplicates())

