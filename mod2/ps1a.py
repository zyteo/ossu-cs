# Assignment 1 - Part A
# Started 14 Mar 2023 by zyteo
# Completed 16 Mar 2023

# Your program should ask the user to enter the following variables: 
# 1.The starting annual salary (annual_salary) 
annual_salary = float(input("Please enter your annual salary: "))
# if annual_salary is not a valid value, print an error message and exit the program
if annual_salary <= 0:
    print("Error: annual salary must be greater than 0")
    exit()

# 2.The portion of salary to be saved (portion_saved) 
portion_saved = float(input("Please enter the portion of your salary to be saved (if 10%, write 0.1): "))
# if portion_saved is not a valid value, print an error message and exit the program
if portion_saved <= 0 or portion_saved > 1:
    print("Error: portion saved must be greater than 0 and not more than 1")
    exit()

# 3.The cost of your dream home (total_cost)
total_cost = float(input("Please enter the cost of your dream home: "))
# if total_cost is not a valid value, print an error message and exit the program
if total_cost <= 0:
    print("Error: total cost must be greater than 0")
    exit()

# need to calculate the months required for the down payment
# need to initialise some variables to help in calculations
r = 0.04
portion_down_payment = 0.25
down_payment = total_cost * portion_down_payment
current_savings = 0
monthly_salary = annual_salary / 12
monthly_savings = monthly_salary * portion_saved
r_monthly = r / 12
months = 0

# can't use a for loop because we don't know how many months it will take
# so i use a while loop that runs as long as the current savings is less than the down payment
while current_savings < down_payment:
    current_savings = current_savings * (1 + r_monthly) + monthly_savings
    months += 1

print("Number of months: ", months)