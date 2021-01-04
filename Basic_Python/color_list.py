# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-04 19:04:04
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-04 19:48:40
# @Title: Display the first and last colors from the following list

# function to display first and last color
def colours_lists():
    values = input("Enter comma seperated colors: ")
    color_list = values.split(",")  #["red", "green", "white", "black"]
    print("Color List is: ", color_list)
    print("First color in List is: ", color_list[0])
    print("Last color in List is: ", color_list[-1])

colours_lists()