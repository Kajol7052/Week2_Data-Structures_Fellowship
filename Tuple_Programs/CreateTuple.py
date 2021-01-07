# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-06 22:20:56
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-06 22:47:58
# @Title: Program to create a tuple

class CreateTuple:

    def __init__(self):
        pass

    def create_tuple(self, size):
        my_tuple = ()
        for j in range(size):
            value = int(input("Enter the value in the tuple: "))
            my_tuple = my_tuple[:j] + (value, )
        print("Created tuple is: ", my_tuple)

if __name__ == "__main__":
    size = int(input("Enter the size of the tuple: "))
    TupleCreate = CreateTuple()
    TupleCreate.create_tuple(size)
    





