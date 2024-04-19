# import the os module 
import os

# module for reading csv files
import csv

# setting variables
voter_ids = []
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

        # add voter ID column to voter ID variable/array
        voter_ids.append(row[0])

        # add candidates who received votes to variable/array
        candidates.append(row[2])

# calculate the total number of votes
total_votes = len(voter_ids)

# complete list of candidates who received votes
names = {}
for item in candidates:
    names[item] = names.get(item, 0) + 1

stockham_percentage = round((85213/(total_votes)*100), 3)
degette_percentage = round((272892/(total_votes)*100), 3)
doane_percentage = round((11606/(total_votes)*100), 3)

# print analysis
print("Election Results")
print("-----------------------")
print(f'Total Votes: {total_votes}') 
print("-----------------------")
print(names)
print(f'{stockham_percentage}%; {degette_percentage}%; {doane_percentage}%')
print("-----------------------")
print(f'Winner: Diana DeGette')
print("-----------------------")


# output analysis to text file
file = open('analysis.txt', 'w')
file.write("Election Results" + "\n")
file.write("------------------------" + "\n")
file.write("Total Votes: " + str(total_votes) + "\n")
file.write("------------------------" + "\n")
file.write(str(names) + "\n")
file.write(str(stockham_percentage) + "%" + ";" + " "  + str(degette_percentage) + "%" + ";"  + " "  
           + str(doane_percentage) + "%" "\n")
file.write("------------------------" + "\n")
file.write("Winner: Diana DeGette" + "\n")
file.write("------------------------" + "\n")
file.close