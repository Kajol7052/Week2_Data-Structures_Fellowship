# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-07 16:14:17
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-07 22:44:46
# @Title: Program to reverse a string

import CustomExceptions

class ReverseString:

    def __init__(self,my_str):
        self.my_str = my_str

    def reverse_string(self):
        """
        :my_str: Reverse the string
        :return : return reversed string
        """
        rev_str = ''
        index = len(self.my_str)
        if index <= 0 :
            raise CustomExceptions.IndexError
        while index > 0:
            rev_str += self.my_str[index - 1]
            index = index - 1
        return rev_str


if __name__ == "__main__":
    try:
        my_str = input("Enter a string: ")
        StringReverse = ReverseString(my_str)
        print("Reverse String is: ", StringReverse.reverse_string())
    except IndexError:
        print("Index Error!")
        