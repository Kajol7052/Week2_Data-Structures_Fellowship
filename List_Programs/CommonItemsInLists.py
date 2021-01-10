# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-08 13:12:33
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-08 13:41:01
# @Title: Program to find common items from two lists


class CommonItemsList:

    def common_items_in_list(self,my_list_1,my_list_2):
        common_list = set(my_list_1) & set(my_list_2)
        print(common_list)

    def create_list(self,my_list):
        """
        funtion take a input from user and generates list
        my_list: lists
        return: list created by user
        """
        my_list = []
        size = int(input("Enter the size of the list: "))
        for i in range(size):
            my_list.append(input("Enter the value in the list: "))
        return my_list
        
if __name__ == "__main__":
    my_list_1 = my_list_2 = common_list = []
    CommonList = CommonItemsList()
    my_list_1 = CommonList.create_list(my_list_1)
    my_list_2 = CommonList.create_list(my_list_2)
    CommonList.common_items_in_list(my_list_1,my_list_2)