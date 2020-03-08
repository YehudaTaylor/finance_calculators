################################################
# Program name: finance_calculators.py
# Written by: Y Taylor
# Date written: 17/01/2020
# This program helps users calculate the return on an investment as well as a loan repayment calculator
# task 
#################################################
import math
print("Choose either 'investment' or 'bond' from the menu below to proceed: \ninvestment      - to calculate the amount of interest you'll earn on intrest:  \nbond         - to calculate the amount you'll have to pay on a home loan: " )
# Promts user to choose a type of calculator
investment_type = input("Please choose either (investment) or (bond): ")
# Promt user for vairables needed for investment calculations
if investment_type.lower() == "investment":
    amount = float(input("Please enter the amount of money you are depositing:"))
    interest_rate = float(input("Please enter the intrest rate percentage (just the number without the % )"))/100
    years_of_investment = float(input("Please enter the number of years you plan on investing for: "))
    interest_type = input("Please choose between (compound) and (simple) interest: ")
    # Simple interest calculation
    if interest_type.lower() == "simple":
        simple_interest = amount * (1 + (interest_rate * years_of_investment))
        print(f"Your simple_interest is: {simple_interest:.2f}")
    # Compound interest caculation    
    elif interest_type.lower() == "compound":
        compound_interest = amount * (math.pow((1 + interest_rate ),years_of_investment))
        print(f"Your compound_interest is: {compound_interest:.2f}")
# Bond calculator
elif investment_type.lower() == "bond":
    # Promt user for bond data 
    present_house_value = float(input("Please enter the current value of the house: "))
    interest_rate = float(input("Please enter the intrest rate percentage (just the number without the % )"))/1200
    number_of_months = float(input("Please enter the number of months you plan on investing for: "))
    # Bond calculator and output value
    repayment = present_house_value*(interest_rate *((1 + interest_rate) ** number_of_months))/(((1 + interest_rate)** number_of_months)- 1)
    print(f"You will need to pay: {repayment:.2f} per month")