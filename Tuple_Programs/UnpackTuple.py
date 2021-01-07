# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-06 22:20:49
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-07 10:37:06
# @Title: Program to unpack a tuple in several variables

class UnpackTup:

    def __init__(self,my_tuple):
        self.my_tuple = my_tuple

    def unpack_tuple_in_variables(self):
        (name, age, *branch) = self.my_tuple
        print(name)
        print(age)
        print(branch)

if __name__ == "__main__":
    try:
        my_tuple = ("Kajol", 21, "Information", "Science", "and", "Engineering")
        TuplesUnpack = UnpackTup(my_tuple)
        TuplesUnpack.unpack_tuple_in_variables()
    except ValueError:
        print("Error")
    
