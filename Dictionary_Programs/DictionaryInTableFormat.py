# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-05 18:51:52
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-06 10:25:15
# @Title: Program to print a dictionary in table format. 

class Table:
     def tableConversion(self,my_dict):
          '''
          Program to print Dictionary
          into Table format
          '''
          print(table.tableConversion.__doc__)
          print ("{:<10} {:<10} {:<10}".format('NAME', 'AGE', 'COUNTRY')) 
          print("------------------------------")  
     # print each data item
          for key, value in my_dict.items(): 
               name, age, country = value 
               print ("{:<10} {:<10} {:<10}".format(name, age, country)) 

# Insert data into dicitonary 
my_dict = {1: ["Elle", 22, 'US'], 
     2: ["Jassie", 25, 'UK'], 
     3: ["Woody", 35, 'UAE'], 
     } 
  
# Print the names of the columns. 
table = Table()
table.tableConversion(my_dict)


