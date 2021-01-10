# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-04 18:58:29
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-04 19:54:23
# @Title: Print the calendar of a given month and year

import calendar # importing the calendar module

# function to print the month of year
def calendar_of_month_and_year():
    year = int(input("Enter the year : "))
    month = int(input("Enter the month : "))
    print(calendar.month(year,month))


calendar_of_month_and_year()