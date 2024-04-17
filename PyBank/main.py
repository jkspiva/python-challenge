# import the os module
import os

# module for reading csv files
import csv

# setting variables
months = []
profit_losses = []
changes = []

# set path to read csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

# read data from csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # skip header row
    header = next(csvfile)

    # start reading from row after header row     
    for row in csvreader:

        # add date column to month variable/array
        months.append(row[0])

        # add profit/losses column to profit_losses variable/array
        profit_losses.append(int(row[1]))

# calculate the total number of months
total_months = len(months)

# calculate the net total profit/losses
net_total = sum(profit_losses)

# calculate average percentage change
for x in range(1, total_months):
    change = profit_losses[x] - profit_losses[x-1]
    changes.append(change)

# calculate average percentage change
average_change = sum(changes)/len(changes)

# greatest increase in profits
greatest_increase = max(changes)
greatest_increase_date = 

#


print(f'{total_months}')
print(f'{net_total}')
