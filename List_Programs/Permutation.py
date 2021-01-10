# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-06 19:56:56
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-08 10:16:55
# @Title: Program to generate all permutations of a list in Python  

import itertools 

class PermutationList:

    def __init__(self):
        size = int(input("Enter the size of the lists: "))
        lists = []
        for i in range(1, size+1):
            lists.append(input("Enter the values in the lists: "))
        self.lists = lists
        print("List is: ", self.lists)
        
    def get_permutation(self):
        perm_list = (list(itertools.permutations(self.lists)))
        return perm_list


if __name__ == "__main__":
    
    ListData = PermutationList()
    print("The Updated List Are : ", ListData.get_permutation())
