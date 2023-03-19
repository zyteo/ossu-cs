# Assignment 1 - Part C
# Started 19 Mar 2023 by zyteo
# Completed x Mar 2023

# Your program should ask the user to enter the following variables: 
# 1.The starting annual salary (annual_salary) 
annual_salary = float(input("Please enter your annual salary: "))
# if annual_salary is not a valid value, print an error message and exit the program
if annual_salary <= 0:
    print("Error: annual salary must be greater than 0")
    exit()

# To simplify things, assume:
# 1.Your semiannual raise is .07 (7%) 
# 2.Your investments have an annual return of 0.04 (4%) 
# 3.The down payment is 0.25 (25%) of the cost of the house 
# 4.The cost of the house that you are saving for is $1M.

# need to calculate the best savings rate (portion_saved) to achieve the down payment in 36 months
# need to initialise some variables to help in calculations
r = 0.04
total_cost = 1000000
semi_annual_raise = 0.07
portion_down_payment = 0.25
down_payment = total_cost * portion_down_payment
current_savings = 0
monthly_salary = annual_salary / 12
# monthly_savings = monthly_salary * portion_saved
r_monthly = r / 12
months = 12 * 3

# planning process
# high = 10000, low = 0, epsilon = 100, and first guess will be (high + low) / 2 = 5000. converted % is guess / 100
# before that, first use 100%, if 100% is not enough means can't afford the down payment in 3 years, return error message
# use convert % to see if can get 250k in 36 months
# if > 250k, decrease guess by half
# if < 250k, increase guess by half
# add to the counter
# rinse and repeat...

# first write a function to calculate the total savings after 36 months
def calculate_savings(savings_rate):
    for months in range(36):
        if (months % 6) == 0 and months != 0:
            annual_salary = annual_salary * (1 + semi_annual_raise)
            monthly_salary = annual_salary / 12
            monthly_savings = monthly_salary * savings_rate
            current_savings = current_savings * (1 + r_monthly) + monthly_savings
        else:
            current_savings = current_savings * (1 + r_monthly) + monthly_savings
    return current_savings
        
