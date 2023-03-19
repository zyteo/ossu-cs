# Assignment 1 - Part C
# Started 19 Mar 2023 by zyteo
# Completed 19 Mar 2023

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
total_cost = 1000000
portion_down_payment = 0.25
down_payment = total_cost * portion_down_payment

# planning process
# high = 10000, low = 0, epsilon = 100, and first guess will be (high + low) / 2 = 5000. converted % is guess / 100
# before that, first use 100%, if 100% is not enough means can't afford the down payment in 3 years, return error message
# use convert % to see if can get 250k in 36 months
# if > 250k, decrease guess by half
# if < 250k, increase guess by half
# add to the counter
# rinse and repeat...

# so for visualisation, the process is:
# first case low1 ============================== guess1 ================================ high1
# if > 250k, low1 ============guess2============ high2 = guess1 ========================= high1
# if < 250k, low1 ======================== low2 = guess1 =============guess2============ high1
# rinse and repeat...

# first write a function to calculate the total savings after 36 months
def calculate_savings(savings_rate, annual_salary):
    current_savings = 0
    r = 0.04
    semi_annual_raise = 0.07
    monthly_salary = annual_salary / 12
    monthly_savings = monthly_salary * savings_rate
    r_monthly = r / 12
    months = 12 * 3
    for month in range(months):
        if (month % 6) == 0 and month != 0:
            annual_salary = annual_salary * (1 + semi_annual_raise)
            monthly_salary = annual_salary / 12
            monthly_savings = monthly_salary * savings_rate
            current_savings = current_savings * (1 + r_monthly) + monthly_savings
        else:
            current_savings = current_savings * (1 + r_monthly) + monthly_savings
    return current_savings
        
# now write the function for the bisection search
def bisection_search(annual_salary):
    high = 10000
    low = 0
    epsilon = 100
    guess = (high + low) / 2
    converted_guess_percentage = guess / 100
    num_guesses = 0
    first_savings_calculation = calculate_savings(1, annual_salary)
    if first_savings_calculation < down_payment:
        print("It is not possible to pay the down payment in three years.")
        exit()
    else:
        savings_calculation = calculate_savings(converted_guess_percentage,annual_salary)
        while abs(savings_calculation - down_payment) >= epsilon:
            if savings_calculation > down_payment:
                high = guess
                guess = (high + low) / 2
                converted_guess_percentage = guess / 100
                num_guesses += 1
                savings_calculation = calculate_savings(converted_guess_percentage,annual_salary)
            else:
                low = guess
                guess = (high + low) / 2
                converted_guess_percentage = guess / 100
                num_guesses += 1
                savings_calculation = calculate_savings(converted_guess_percentage,annual_salary)
        print("Best savings rate:", converted_guess_percentage)
        print("Steps in bisection search:", num_guesses)
    
bisection_search(annual_salary)