# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-07 21:36:52
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-07 22:56:27
# @Title: Program that accepts a comma separated sequence of words as input and prints the unique words in sorted form
#   Sample Words : red, white, black, red, green, black
#	Expected Result : black, green, red, white
import CustomExceptions
class StringList:
    def __init__(self,my_str):
        self.my_str = my_str
    def sortWordUnique(self):
        word_list = []
        #loop for adding elements from comma seperated userInput
        for words in self.my_str.split(','):
            if words not in word_list: #checks for unique words in userInput
                word_list.append(words)
try:
    my_str=input("Enter the words seperated by comma")
    if my_str.isdigit == True:
        raise CustomExceptions.ValueError()
    stringList = StringList(my_str)
    stringList.sortWordUnique()
except CustomExceptions.ValueError:
    print("Value Error")