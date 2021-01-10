# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-05 20:08:48
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-06 10:08:26
# @Title: Program to count number of items in a dictionary value that is a list

# Python program to count number of items 
# in a dictionary value that is a list. 

class Counter:
	def countItems(self,d):
		count = 0
		for x in d: 
			if isinstance(d[x], list): 
				count += len(d[x]) 
		print(count) 

def main(): 
	# defining the dictionary 
	d = {'A' : ["a", "b", "c", "d"], 
		'B' : 25, 
		'C' : 12, 
		'D' : ["True", "False", 1, 2] } 

	# using the membership operator 
	counter = Counter()
	counter.countItems(d)
	print(counter.countItems.__doc__)

# Calling Main	 
if __name__ == '__main__': 
	main() 
