# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-06 18:27:43
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-08 10:36:23
# @Title: Program to clone or copy a list

class CloneLists:
    def __init__(self):
        original_list = []
        size = int(input("Enter the size of the lists: "))
        for items in range(size):
            original_list.append(input("Enter the values in the list: "))
        self.original_list = original_list
        
    def cloning_list(self): 
        updated_list = [] 
        updated_list.extend(self.original_list) 
        return updated_list 
  
if __name__ == "__main__":
    
    ListClone = CloneLists()
    updated_list = ListClone.cloning_list() 
    print("Original list is:", ListClone.original_list) 
    print("After cloning is:", updated_list) 