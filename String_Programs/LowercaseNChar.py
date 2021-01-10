# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-07 16:25:54
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-07 22:43:45
# @Title: Program to lowercase first n characters in a string

import CustomExceptions

class LowerCase:

    def __init__(self,my_str):
        self.my_str = my_str

    def lowercase_first_n_char(self):
        n = int(input("Enter the n to lowercase the first n characters: ")) 
        new_str = self.my_str[:n+1].lower() + self.my_str[n+1:] 
        print("The updated string after lowercase first n character is: ", str(new_str))


if __name__ == "__main__":
    try:
        my_str = input("Enter the string: ")
        if(my_str.isdigit()):
            raise CustomExceptions.ValueError()
        ConvertLower = LowerCase(my_str)
        ConvertLower.lowercase_first_n_char()
    except CustomExceptions.ValueError:
        print("ValueError occured")