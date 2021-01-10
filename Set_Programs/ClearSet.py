# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-05 20:49:27
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-05 22:39:25
# @Title: Program to clear a set


class SetClear:
    def clear_set(self):
        my_set = set()
        size = int(input("Enter the size of the set: "))
        for i in range(size):
            my_set.add(int(input("Enter the unique elements in set: ")))
        return my_set

set_1 = set()
setClear = SetClear()
set_1 = setClear.clear_set()
print(setClear.clear_set.__doc__)
print(set_1)
choice=input("Do you want to clear the set ? Enter y for yes: ")
if choice == "y": #check if choice y if y then clears the set
    set_1.clear() #clear the set
    print("Cleared all elements: ", set_1)
else:
    print("Set is: ", set_1)