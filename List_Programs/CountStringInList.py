# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-06 17:42:12
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-08 09:56:25
# @Title: Program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings

class ListCount:

    def __init__(self,string_list):
       self.string_list = string_list 

    def count_string(self):
        count=0
        for x in self.string_list: 
             if len(x) >= 2 and x[0] == x[-1]: #checks if each element length is more than 2 and first and last character is same
                count+=1
        return count

if __name__ == "__main__":
    string_list = ['abc', 'xyz', 'aba', '1221']
    CountString = ListCount(string_list)
    print("The element present in list is:", CountString.count_string())