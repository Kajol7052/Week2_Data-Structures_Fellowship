# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-08 22:57:47
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-09 00:24:52
# @Title: Program to remove duplicates from a list of lists

class ListOfList:
    def __init__(self):
        self.my_list = [[1,2],[3,4],[4,2],[2,4],[4,1],[3,4]]

    def duplicateList(self,list_1,list_2):
        if len(list_1) != len(list_2):
            return False
        else:
            for i in range(len(list_2)):
                if list_1[i] != list_2[i]:
                    return False
            return True
        
    def printUniqueList(self):
        unique_list = []
        for i in range(len(self.my_list)):
            isUnique = True
            for j in range(i+1,len(self.my_list)):
                if self.duplicateList(self.my_list[i],self.my_list[j]):
                    isUnique = False
            if isUnique :
                unique_list.append(self.my_list[i])
        print(unique_list)
listOfList = ListOfList()
listOfList.printUniqueList()