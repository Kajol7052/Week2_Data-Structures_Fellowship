# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-07 21:03:06
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-07 22:40:44
# @Title:  Prohram that takes a list of words and returns the length of the longest one

import CustomExceptions

class LongestString:

    def __init__(self,my_list):
        self.my_list = my_list

    def longest_length_string(self):
        """
        prints the length of longest word
        :my_list: list
        """
        max = len(self.my_list[0]) #assigns the length of first element from list
        for word in self.my_list:
            if len(word) >= max: 
                max = len(word)
                max_ele = word
        print("Longest word in list is", max_ele ,"and length is: ", max)


        


if __name__ == "__main__":
    try:
        size = int(input("Enter the size of list: "))
        string_list = []
        for i in range(size):
            string_list.append(input("Enter the word in the list: "))
        LargestString = LongestString(string_list)
        print(LargestString.longest_length_string())
    except ValueError:
        print("Value error")