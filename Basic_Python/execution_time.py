# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-04 19:06:12
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-04 20:46:53
# @Title: Program to get execution time for a Python method

import time

# starting time
start = time.time()

# program body starts
for i in range(10):
    print(i)

# sleeping for 1 sec 
time.sleep(1)

# end time
end = time.time()

# total time taken
print(f"Runtime of the program is {end - start}")