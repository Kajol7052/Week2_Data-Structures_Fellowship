# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-06 19:42:43
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-08 10:13:51
# @Title: Program to print a specified list after removing the 0th, 4th and 5th elements.  
#	Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#	Expected Output : ['Green', 'White', 'Black']


class RemoveElement:

    def __init__(self,my_list,new_list):
        self.my_list = my_list
        self.new_list = new_list

    def remove_specific_element(self):
        for index, value in enumerate(self.my_list):
            print(index, value)
            if index not in [0, 4, 5]:
                self.new_list.append(value)
        print(self.new_list)


if __name__ == "__main__":
    my_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    new_list = []
    RemoveItem = RemoveElement(my_list,new_list)
    RemoveItem.remove_specific_element()
