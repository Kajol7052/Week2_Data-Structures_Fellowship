# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-04 18:58:19
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-04 19:57:03
# @Title: Calculate number of days between two dates

from datetime import date  # from datetime module import date type

first_date = date(2014, 7, 2)
last_date = date(2014, 7, 11)
difference = last_date - first_date # difference between dates
print("The difference between two date is : ", difference.days, "days")