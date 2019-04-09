
# This is a program to calculate the profit of sales, in percentage, for a

# company that wants a program, for this specific purpose.

# April 8th, 2019.

# CTI-110 P2T1-Sales Prediction

# Leland Morel

# Pseudocode = 1: Get total projected sales. 2: Calculate profit using given

# percentage of 0.23 .

# 3: Display profit.




  
#get projected total sales

total_sales = float(input('Enter projected total sales: '))

# calculate profit using given percentage number, 0.23

profit = total_sales * 0.23

# display profit
print ('The profit is: $', format(profit,'14,.2f'))
