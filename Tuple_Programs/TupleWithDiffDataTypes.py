# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-06 22:20:52
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-07 10:34:58
# @Title: Program to create a tuple with different data types

import CustomExceptions
class DiffDataTypes:

    def __init__(self,int_val,float_val,str_val,bool_val):
        self.int_val = int_val
        self.float_val = float_val
        self.str_val = str_val
        self.bool_val = bool_val

    def create_tuple_diff_data_types(self):
        my_tuple = (self.int_val,self.float_val,self.str_val,self.bool_val)
        print("Created tuple with different Data Types is: ", my_tuple)

if __name__ == "__main__":
    try:
        int_val = int(input("Enter int value: "))
        float_val = float(input("Enter float value: "))
        str_val = input("Enter string: ")
        bool_val = bool(input("Enter boolean value: "))
        DataTypes = DiffDataTypes(int_val,float_val,str_val,bool_val)
        DataTypes.create_tuple_diff_data_types()
    except ValueError:
        print("Enter the correct value")
    
    