# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-06 22:20:44
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-07 10:07:23
# @Title: Program to find the repeated items of a tuple

import CustomExceptions

class RepeatTuple:
    
    def __init__(self, my_tuple):
        self.new_tuple = my_tuple

    def find_repeated_items(self, new_tuple):
        """
        prints the repeated items in list
        new_tuple: 
        """
        my_list = [] #empty list to store unique value from tuples
        print("Repeated element is: ")
        for x in self.new_tuple:
            if x not in my_list and self.new_tuple.count(x) > 1:
                print(x)
                my_list.append(x)
        print(my_list)

if __name__ == "__main__":
    try:   
        my_list = [] #creates empty list
        size = int(input("Enter the size of tuple: "))
        if size < 0:
            raise CustomExceptions.NegativeValueError()
        for i in range(size):
            my_list.append(input("Enter the values: "))

        my_tuple = tuple(my_list) #coverts list to tuple and then assigns to tuples_1
        print(my_tuple)
        TupleRepeat = RepeatTuple(my_tuple)
        TupleRepeat.find_repeated_items(my_tuple) #function call
    except CustomExceptions.NegativeValueError:
        print("Negative Value error")