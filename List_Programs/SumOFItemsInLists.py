# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-06 11:13:50
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-08 09:49:31
# @Title: Program to sum all the items in a list

import CustomExceptions

class ListsSum:

    def __init__(self):
        size = (int(input("Enter the size of lists: ")))    # stores the size of list
        my_list = []    # created empty lists
        for i in range(size):
            try:
                my_list.append(int(input("Enter the integer value in list: ")))
            except ValueError:
                print("Enter only integer values")
            continue
        print("Lists is: ", my_list)
        self.my_list = my_list

    def sum_of_list(self):
        """
        returns the sum of all the elements in list
        """
        length = len(self.my_list)
        sum = 0
        for i in range(length):
            sum = sum + self.my_list[i]
        return sum


if __name__ == "__main__":
    
    SumLists = ListsSum()
    print("Sum elements in the list is: ", SumLists.sum_of_list()) # function call and prints the sum of elements
    
