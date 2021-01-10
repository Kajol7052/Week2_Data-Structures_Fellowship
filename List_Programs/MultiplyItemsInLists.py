# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-06 11:42:20
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-08 10:33:07
# @Title: Pprogram to multiplies all the items in a list


class ListsMultiply:

    def __init__(self):
        size = int(input("Enter the size of lists: "))   # stores the size of list
        my_list = []    # created empty lists
        for i in range(size):
            try:
                my_list.append(int(input("Enter the integer value in list: ")))
            except ValueError:
                print("Enter only integer values")
                continue
        print("Lists is: ", my_list)
        self.my_list = my_list
        
    def product_of_list(self):
        """
        returns the multiplication of all the elements in list
        
        """
        length = len(self.my_list)
        mul = 1
        for i in range(0,length):
            mul = mul * self.my_list[i]
        return mul


if __name__ == "__main__":
 
    MulLists = ListsMultiply()
    print("Sum elements in the list is: ", MulLists.product_of_list()) # function call and prints the product of elements
