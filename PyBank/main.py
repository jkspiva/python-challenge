#import the os module
import os

#module for reading CSV files
import csv

#set path for file
csvpath = os.path.join('Resources', 'budget_data.csv')

#open and read CSV
with open(csvpath) as csvfile:
    
    #CSV reader specifies variable that holds content and delimiter
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #read the header row first
    csv_header = next(csvfile)

    total_months = len(list(csvreader))
    #net_total = sum(int(row[1]) for row in csvreader)
    
    #read each row of data after the header
    for row in csvreader:
        net_total = sum(int(row[1]) for row in csvreader)
        print(f"{net_total}")
    
print("Financial Analysis")
print("--------------------------------------------")

print(f"Total Months: {total_months}")
print(f"{net_total}")