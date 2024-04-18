# import the os module 
import os

# module for reading csv files
import csv

# setting variables
votes = []
candidates = []

# set path to read csv file
csvpath = os.path.join('Resources', 'election_data.csv')

# read data from csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # skip header row
    header = next(csvfile)

    # start reading from row after header
    for row in csvreader:

        # add voter ID column to total votes variable/array
        votes.append(row[0])

        # add candidates who received votes to variable/array
        candidates.append(row[2])

# calculate the total number of votes
total_votes = len(votes)

# complete list of candidates who received votes





print("Election Results")
print("-----------------------")
print(f'Total Votes: {total_votes}') 
print("-----------------------")



print("-----------------------")
print(f'Winner: ')
print("-----------------------")