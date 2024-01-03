"""This module provides access to the mathematical functions defined by the C standard."""
import math

# Print the menu and ask the user to choose a calculation

MENU = '''
investment - to calculate the amount of interest you'll earn on your investment
bond       - to calculate the amount you'll have to pay on a home loan

'''
print(MENU)
calculation = input("Enter either 'investment' or 'bond' from the menu above "
                    "to proceed: ")
calculation = calculation.lower()
print()

# Show an error message if necessary and ask user to try again

while calculation not in ("investment", "bond"):
    calculation = input("Error - please enter either 'investment' or 'bond' to proceed: ")
    calculation = calculation.lower()
    print()

# Run the chosen calculator

# Investment calculator

if calculation == "investment":

    # Take in deposit, interest rate, investment length and interest type

    deposit = float(input("How much money are you depositing? £"))
    print()
    interest_rate = float(input("What is the percentage interest rate? "))
    interest_rate = interest_rate / 100
    print()
    investment_length = int(input("How many years do you plan on investing? "))
    print()
    interest = input("Do you want simple or compound interest? ")
    interest = interest.lower()
    print()

    # Show error message if necessary and ask user to try again

    while interest not in ("simple", "compound"):
        interest = input("Error - please enter either 'simple' or 'compound' to proceed: ")
        interest = interest.lower()
        print()

    # Simple interest calculation

    if interest == "simple":
        investment_return = deposit * (1 + interest_rate * investment_length)

    # Compound interest calculation

    else:
        investment_return = deposit * math.pow((1 + interest_rate), investment_length)

    # Output investment return

    print(f"The return on your £{deposit:.2f} investment after {investment_length} years will be: "
          f"£{investment_return:.2f}")
    print()

# Bond calculator

else:

    # Take in value of house, interest rate and repayment length

    value = float(input("What is the value of the house? £"))
    print()
    interest_rate = float(input("What is the percentage interest rate? "))
    monthly_interest_rate = interest_rate / 1200
    print()
    repayment_length = int(input("How many months do you plan to take to repay the bond? "))
    print()

    # Repayment calculation

    monthly_repayment = (monthly_interest_rate * value) / (1 - (1 + monthly_interest_rate) ** \
                                                           (- repayment_length))

    # Output monthly repayment

    print(f"The monthly repayment on your £{value:.2f} house over {repayment_length} months will "
          f"be: £{monthly_repayment:.2f}")
    print()
