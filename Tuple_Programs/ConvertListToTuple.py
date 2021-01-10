# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-06 22:20:33
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-07 00:55:33
# @Title:

import CustomExceptions
class ListToTuple:

    def __init__(self,my_list):
        self.my_list = my_list

    def convert_to_tuple(self):
        """
        my_list: element the value
        return: tuple value
        """
        my_tuple = tuple(self.my_list)
        print("Tuple is: ", my_tuple)

if __name__ == "__main__":
    try:
        size = int(input("Enter the size of list: "))
        if size < 0 :
            raise CustomExceptions.NegativeValueError()
        my_list = []
        for i in range(size):
            value = int(input("Enter the element: "))
            my_list.append(value)

        print("List is: ", my_list)
        Conversion = ListToTuple(my_list)
        Conversion.convert_to_tuple()
    except CustomExceptions.NegativeValueError:
        print("Negative value error ")
    