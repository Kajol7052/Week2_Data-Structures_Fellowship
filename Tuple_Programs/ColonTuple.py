# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-06 22:20:46
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-07 10:13:36
# @Title: 

from copy import deepcopy
from copy import copy

#create a tuple
my_tuple = ("KAJOL", 5, [], True) 
print(my_tuple)
colon_tup = deepcopy(my_tuple)
colon_tup[2].append(50)
print("---After Deep Copy---")
print("DeepCopied: " , colon_tup)
print("Original Tuple:", my_tuple)
shallow_tup = copy(my_tuple)
shallow_tup[2].append(10)
print("---After Shallow Copy---")
print("ShallowCopied: " , shallow_tup)
print("Original Tuple:",my_tuple)

    