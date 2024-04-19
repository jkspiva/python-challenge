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
    header = next(csvreader)

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

# rounding average change to 2 decimal places
num = average_change 
rounded_num = round(average_change, 2)

# greatest increase in profits
greatest_increase = max(changes)
greatest_increase_date = months[changes.index(greatest_increase) + 1]
greatest_decrease = min(changes)
greatest_decrease_date = months[changes.index(greatest_decrease) + 1]

# print analysis
print(f'Financial Analysis')
print("---------------------------------------------------")
print(f'Total Months: {total_months}')
print(f'Total: ${net_total}')
print(f'Average Change: ${rounded_num}')
print(f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})')

# output analysis to text file
file = open('analysis.txt', 'w')
file.write("Financial Analysis" + "\n")
file.write("-----------------------------------" + "\n")
file.write("Total Months: " + str(total_months) + "\n")
file.write("Total: " + "$" + str(net_total) + "\n")
file.write("Average Change: " + "$" + str(rounded_num) + "\n")
file.write("Greatest Increase in Profits: " + str(greatest_increase_date) + " " + "$" + str(greatest_increase) + "\n") 
file.write("Greatest Decrease in Profits: " + str(greatest_decrease_date) + " " + "$" + str(greatest_decrease) + "\n")
file.close