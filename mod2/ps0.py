# Assignment 0
# Started 7 Mar 2023 by zyteo
# Completed 7 Mar 2023

import numpy
# Write a program that does the following in order:
# 1. Asks the user to enter a number “x”
input_x = int(input("Please enter a number for x: "))
# 2. Asks the user to enter a number “y”
input_y = int(input("Please enter a number for y: "))
# 3. Prints out number “x”, raised to the power “y”.
print(input_x, "to the power of", input_y, "is", input_x**input_y)
# 4. Prints out the log (base 2) of “x”.
print("The log, to base 2, of", input_x, "is", numpy.log2(input_x))