# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-04 19:04:24
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-04 20:32:49
# @Title: Program to find out the number of CPUs using


import multiprocessing
import os

# multiprocessing.cpu_count is nothing but a wrapper around os.cpu_count
print(multiprocessing.cpu_count()) # Return the number of CPUs in the system. May raise NotImplementedError.
print(os.cpu_count()) # Return the number of CPUs in the system.