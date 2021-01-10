# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-07 19:50:24
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-07 22:31:51
# @Title: Program to count occurrences of a substring in a string

import CustomExceptions

class Substring:

    def __init__(self,my_str,sub_str):
        self.my_str = my_str
        self.sub_str = sub_str
    #Create this method to find the occurence of substring
    def substring_occurence(self):
        """
        :my_str: string
        :sub_str: sub string in string
        :return: return the count of substring
        """
        print("Substring count is: ",self.sub_str," is: ",self.my_str.count(sub_str))

if __name__ == "__main__":
    try:
        my_str = input("Enter a string: ")
        sub_str = input("Enter a substring: ")
        SubStringOccurence = Substring(my_str, sub_str)
        SubStringOccurence.substring_occurence()
    except CustomExceptions.ValueError:
        print("Value Error")