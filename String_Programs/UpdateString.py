# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-07 22:09:29
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-07 22:59:30
# @Title: 

class Update:
    
    def __init__(self,my_str):
        self.my_str = my_str
    def update_string(self):
        """
        :my_str: string
        :return updated string with ing or ly
        """
        if len(self.my_str) >= 3:
            if self.my_str[len(self.my_str)-3:len(self.my_str)] != "ing":
                self.my_str += "ing"
            else:
                self.my_str += "ly"
        return self.my_str

if __name__ == "__main__":
    try:
        my_str = input("Enter a string: ")
        StringUpdate = Update(my_str)
        print(StringUpdate.update_string())
    except ValueError:
        print("Value Error")
