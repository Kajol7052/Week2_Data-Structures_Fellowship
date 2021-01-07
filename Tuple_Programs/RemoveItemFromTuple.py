# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-06 22:20:31
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-07 11:03:55
# @Title: 

import CustomExceptions
class RemoveItem:
    def __init__(self,new_tuple):
        self.my_tuple = new_tuple
        
    def remove_item_from_tuple(self, value):
        """
        removes an item in list and return updated tuple 
        value: element to be removed from tuple
        return: return updated tuples
        """
        my_list = list(self.my_tuple) #converts tuple to list to do deletion operation
        for x in my_list:
            # checks if value is there in myList , it is required to avoid exception
            if value in my_list:
                my_list.remove(value)
                print("Deleted Successfully")
        my_tuple = tuple(my_list) #converts list to tuples
        return my_tuple

if __name__ == "__main__":
    try:
        new_list = []
        size = (int(input("Enter the size of the list: ")))
        for i in range(size):
            new_list.append(int(input("Enter the integers value in list: ")))
        new_tuple = tuple(new_list) #coverts list to tuple and then assigns to tupleEx
        print(new_tuple)
        element = int(input("Enter the value to be deleted: "))
        ItemRemove = RemoveItem(new_tuple)
        print("After deleting element from tuple", ItemRemove.remove_item_from_tuple(element)) #function call and printd the updated tuples
    except CustomExceptions.ValueError:
        print("Value error raised")
