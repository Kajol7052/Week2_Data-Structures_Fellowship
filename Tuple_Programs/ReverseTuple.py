# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-06 22:20:19
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-07 10:31:01
# @Title: 
import CustomExceptions
class ReverseTuples:

    def __init__(self,new_tuple):
        self.my_tuple = new_tuple

    def reverse_tuples(self, size):
        """
        returns reversed tuple
        """
        reverse_tuple = ()
        reverse_tuple=self.my_tuple[::-1]
        return reverse_tuple



if __name__ == "__main__":
    try:
        new_tuple = tuple()
        my_list = []
        size = int(input("Enter the size of tuple: "))
        if size <= 0:
                raise CustomExceptions.IndexError()
        for x in range(size):
            my_list.append(input("Enter the element in tuple: "))
        new_tuple= tuple(my_list)
        print("Before reversing the tuples: ", new_tuple)
        TupleReverse = ReverseTuples(new_tuple)
        new_tuple = TupleReverse.reverse_tuples(size) #function call
        print("After reversing the tuples: ", new_tuple)
    except CustomExceptions.IndexError:
        print("Index error raised")