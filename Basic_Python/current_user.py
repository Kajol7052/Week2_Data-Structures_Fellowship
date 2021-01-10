# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-04 19:04:45
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-04 20:42:53
# @Title: Program to get the current username

# The getpass() function is used to prompt to users using the string prompt and reads the input from the user as Password. 
# The input read deafults to “Password: ” is returned to the caller as a string.
import getpass

username = getpass.getuser() # The getuser() function displays the login name of the user.
print("The current user is : ", username)