# -*- coding: utf-8 -*-
"""
Add your group member names here

"""

import sys

'''Part A
=============================================================================
Calculate credit card balance after no payment made for a period of months.
=============================================================================
'''
# Display information, solicit input, and be sure it is proper format
total_balance = int(input('Enter your balance:\t'))
months = int(input('Enter the number of months:\t'))
purchase_per_month = float(input('Enter the purchase amount per month:\t'))
interest_rate = float(input('Enter the interest rate:\t'))
interest_rate = interest_rate/100/12
# Loop to calculate ending credit card balance
m = 0
while m < months:
    m+=1
    total_balance = total_balance + purchase_per_month
    total_balance = total_balance + (total_balance*interest_rate)
    
    
# Prepare variables as string for output and output results
currency_notation = "{:.2f}".format(total_balance)

print('The total after',months,'months is $'+currency_notation)

'''Part B
=============================================================================
After a few months, you stop buying and decide to pay off the card.
=============================================================================
'''
# Display information, solicit input, and be sure it is proper format
print('Check to see if the monthly payment is enough to keep balance from growing')

monthly_payment = float(input('Enter a monthly payment:\t'))

currency_monthly_payment = "{:.2f}".format(monthly_payment)

monthly_interest = total_balance*interest_rate


# Check to see if payment is sufficient. If not communicate and quit.
# If sufficient, communicate.
if monthly_payment > monthly_interest:
    print('A monthly payment of $'+currency_monthly_payment+' will work.')
else:
    print('This will not work, you will be paying off card forever')

# Calculate and display minimum payment
currency_monthly_interest = "{:.2f}".format(monthly_interest)

if monthly_payment > monthly_interest:
    print('The monthly minimum payment is $'+currency_monthly_interest)
else:
    print('')
  
'''Part C
=============================================================================
With this monthly payment, determine how long it will take to pay off card.
=============================================================================
'''
# Loop to calculate months needed to pay off card
m = 0
if monthly_payment > monthly_interest:
    while total_balance >= 0:
        total_balance = total_balance - monthly_payment
        total_balance = total_balance + (total_balance*interest_rate)

        m+=1
else:
    print('')
# Prepare variables as string for output and output results as months and years
y = m/12

m = str(m)
y_round = "{:.2f}".format(y)
if monthly_payment > monthly_interest :
    print('It will take '+m+' months to pay off card with $'+currency_monthly_payment+' payments')
    print('It will take '+y_round+' years to pay off card with $'+currency_monthly_payment+' payments')
else:
    print('')
