# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-05 16:36:15
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-05 23:28:24
class Unique:
    def fetchUnique(self,test_list):
        print("The original list : ",test_list)
        result = (set(val for dic in test_list
                for val in dic.values()))
        # printing result
        print("The unique values in list are : " + str(result))

test_list =  [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"},
{"V":"S009"},{"VIII":"S007"}]
unique = Unique()
unique.fetchUnique(test_list)
print(unique.fetchUnique.__doc__)

