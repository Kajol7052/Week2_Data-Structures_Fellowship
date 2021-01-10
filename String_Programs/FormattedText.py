# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-07 19:17:41
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-07 22:36:18
# @Title: Program to display formatted text (width=50) as output
import CustomExceptions
import textwrap
class FormatText:
    def __init__(self,my_str):
        self.my_str = my_str

    def display_formatted_text(self):
        """
        my_str: paragram
        return: formatted text 
        """
        print(textwrap.wrap(self.my_str, width=50))

if __name__=="__main__":
    try:
        my_str = input("Enter a Paragraph: ")
        TextFormatted = FormatText(my_str)
        TextFormatted.display_formatted_text()
    except CustomExceptions.ValueError:
        print("Error occured")



