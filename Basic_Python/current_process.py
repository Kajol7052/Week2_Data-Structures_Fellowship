# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-04 19:04:37
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-04 21:11:39
# @Title: Program to get the effective group id, effective user id, real group id, a list of supplemental group ids associated with the current process.

import os
# Every process group is uniquely identified using process group id.
print("\nEffective group id: ",os.getegid())
print("Effective user id: ",os.geteuid())
print("Real group id: ",os.getgid())
print("List of supplemental group ids: ",os.getgroups())
print()
