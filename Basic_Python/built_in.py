# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-04 18:58:12
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-04 20:59:53
# @Title: Program to find the available built-in modules


# textWrap function wraps the input paragraph such that each line in the paragraph 
# is at most width characters long. The wrap method returns a list of output lines. 
# The returned list is empty if the wrapped output has no content. Default width is taken as 70.
import sys
import textwrap

module_name = ', '.join(sorted(sys.builtin_module_names))
print(textwrap.fill(module_name, width=70))