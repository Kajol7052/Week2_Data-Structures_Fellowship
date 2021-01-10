# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-07 15:36:53
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-07 22:57:17
# @Title: Program to calculate the length of a string


class StringLength:
    
    def __init__(self,my_str):
        self.my_str=my_str

    def length_of_string(self):
        """
        function returns the length of the string
        """
        #print("Length of the string is:", len(my_str))
        counter = 0 # initially count is 0
        for char in self.my_str:
            counter = counter+1
        print("Length of the string is:", counter)

if __name__ == "__main__":
    try:
        my_str = input("Enter a string: ")
        LengthString = StringLength(my_str)
        LengthString.length_of_string()
    except ValueError:
        print("Please enter correct value")