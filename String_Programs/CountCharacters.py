# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-07 15:50:36
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-07 22:28:41
# @Title: Program to count the number of characters(character frequency) in string  
#	Sample String : google.com
#	Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}


class CountCharacters:

    def __init__(self,my_str):
        self.my_str=my_str

    def count_frequency_of_char(self):
        for i in self.my_str: 
            if i in count_freq: 
                count_freq[i] += 1
            else: 
                count_freq[i] = 1
        print ("Frequency count of all characters in", self.my_str, "is:\n ", str(count_freq))




if __name__ == "__main__":
    try:
        count_freq = {}
        my_str = input("Enter the string: ")
        CharCount = CountCharacters(my_str)
        CharCount.count_frequency_of_char()
    except:
        print("Error occured")




#from collections import Counter 
#my_str = input("Enter the string: ")
#count_freq = Counter(my_str) # using collections.Counter() to get count of each element in string  
#print ("Frequency count of all characters in", my_str, "is:\n ", str(count_freq)) 