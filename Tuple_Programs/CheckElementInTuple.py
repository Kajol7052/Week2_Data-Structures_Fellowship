# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-06 22:20:41
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-07 14:48:25
# @Title: 

import CustomExceptions

class CheckElement:

    def __init__(self,tup):
        """
        initialise new_tuple
        """
        self.new_tuple = tup

    def check_element_exist_or_not(self, value):
        """
        returns true if element is present in tuples else return false
        value: check value present in tuple or not
        return: True or False
        """
        found = False
        for x in self.new_tuple:
            if x == value:
                found = True
        return found


if __name__ == "__main__":
    try:
        my_list = [] #creates empty list
        size = int(input("Enter the size of tuple: "))
        if size < 0 :
            raise CustomExceptions.NegativeValueError()
        for i in range(size):
            my_list.append(input("Enter the values:  "))

        new_tuple = tuple(my_list) #converts list to tuple
        print(new_tuple)
        ElementCheck = CheckElement(new_tuple)
        search_element = input("Enter the element to be searched: ")
        print("Element",search_element,"present in tuple?", ElementCheck.check_element_exist_or_not(search_element)) #function call and prints the results
    except CustomExceptions.NegativeValueError:
        print("Negative value error raised")
    