# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-05 15:29:41
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-05 23:18:16
# @Title: Program to Concatenate Dictionaries into a new Dictionary

class ConDict:
    def concate(self,dict1,dict2,dict3):
        concatenate_dict = {}
        for d in (dic1, dic2, dic3):
            concatenate_dict.update(d)
            print("Concatenated Dictionary is: ", concatenate_dict)


dic1 = {1:10, 2:20} 
dic2 = {3:30, 4:40} 
dic3 = {5:50, 6:60}
conDict = ConDict()
conDict.concate(dic1,dic2,dic3)
print(conDict.concate.__doc__)


