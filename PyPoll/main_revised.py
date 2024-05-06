# import the os module 
import os

# module for reading csv files
import csv

# setting variables
voter_ids = []
candidates = []
candidate_votes = {}

winning_candidate = ""
winning_count = 0

# set path to read csv file
csvpath = os.path.join('Resources', 'election_data.csv')

# set output path for analysis
output_analysis = "Resources/analysis.txt"

# read data from csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # skip header row
    header = next(csvfile)

    # start reading from row after header
    for row in csvreader:

        # add voter ID column to voter ID variable/array
        voter_ids.append(row[0])

         # extract the candidate name from each row
        candidate_name = row[2]

        # if candidate does not match an existing candidate
        if candidate_name not in candidates:

            # add to the list of cadidates
            candidates.append(candidate_name)

            # being tracking candidate's vote count
            candidate_votes[candidate_name] = 0

        # then add a vote to that candidate's count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

# total number of votes
total_votes = len(voter_ids)

# print final vote count and export to text file
with open(output_analysis, "w") as txt_file:

    # print final vote count
    election_results = (
        f"\nElection Results\n"
        f"---------------------\n"
        f"Total votes: {total_votes}\n"
        f"---------------------\n"
    )
    print(election_results)

    # save final vote count to text file
    txt_file.write(election_results)

    # Determine winner by looping through the counts
    for candidate in candidate_votes:

        # get vote counts and percentages
        votes = candidate_votes.get(candidate)
        vote_percentage = round(votes/total_votes * 100, 3)

        # determine winning vote count and candidate
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate

        # print each candidates vote count and percentage
        voter_output = (f'{candidate}: {vote_percentage}% ({votes})\n')
        print(voter_output)

        # save voter_output to text file
        txt_file.write(voter_output)
    
    # print winning candidate
    winner = (
        f"---------------------\n"
        f"Winner: {winning_candidate}\n"
        f"---------------------\n"
    )
    print(winner)

    # save winner to text file
    txt_file.write(winner)