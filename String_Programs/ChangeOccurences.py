# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-07 20:47:12
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-07 22:26:10
# @Title: Program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.  
#	Sample String : 'restart'
#	Expected Result : 'resta$t

import CustomExceptions

class ChangeToDollar:

    def __init__(self,my_str):
        self.my_str=my_str

    def change_character(self):
        """
        function replace occurrences of first char in the string to '$'
        :my_str: string
        :return: return the updated string
        """
        first_char = self.my_str[0] # assiging first char to the string
        updated_str = self.my_str[1:len(my_str)] 
        for i in range(len(updated_str)):
            if first_char == updated_str[i]:
                updated_str = updated_str.replace(updated_str[i],"$")

        updated_str = first_char + updated_str # updating string
        return updated_str
    

if __name__ == "__main__":
    try:
        my_str = input("Enter the string: ")
        ReplaceChar = ChangeToDollar(my_str)
        print("After replacing the char, the updated string is: ", ReplaceChar.change_character())
    except ValueError:
        print("")
