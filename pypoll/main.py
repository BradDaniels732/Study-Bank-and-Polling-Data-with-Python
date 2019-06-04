# Main.py for pypoll

# import the modules needed
import os
import csv

# open the csv file
os.chdir(os.path.dirname(__file__))
election_data_filename = os.path.join ("Resources" , "election_data.csv")

# Read the csv file and store the data in lists
with open(election_data_filename, newline='') as election_file:
    election_file_reader = csv.reader(election_file, delimiter=',')

    # Skip the header row
    next(election_file_reader)

    # The columns in the CSV file are "Voter-ID", "County" and "Voted-For"
    # Since we don't need the first two columns, we will only store the third column
    voted_for = []

    # Read each row of data after the header
    for row in election_file_reader:
        voted_for.append(row[2])

# Calculate the total number of votes
num_votes = len (voted_for)

# Find the list of all candidates who received votes
candidates = sorted(list(set(voted_for)))

# Figure out how many votes each candidate received, and calculate the percentage received
votes = []
pct_votes = []

# Figure out who has the most votes
max_votes = 0

for candidate in candidates:
    votes_for_candidate = sum(1 for vote in voted_for if candidate == vote)
    votes.append(votes_for_candidate)
    pct_votes.append(votes_for_candidate/num_votes*100)

    # Is this candidate the winner???
    if (votes_for_candidate > max_votes):
        winning_candidate = candidate
        max_votes = votes_for_candidate

# Put the election results into a list of strings
final_report = []
final_report.append (f"Election Results")
final_report.append (f"--------------------------")
final_report.append ("Total votes: {:,}".format(num_votes))
final_report.append (f"--------------------------")
i = 0
for candidate in candidates:
    final_report.append ("Candidate {0:}, Pct of vote = {1:,.2f}%, Raw Vote = {2:,}".format(candidate,pct_votes[i],votes[i]))
    i += 1
final_report.append (f"--------------------------")
final_report.append (f"Winner: {winning_candidate}")
final_report.append (f"--------------------------")

# Print the results to a text file and the Terminal Window simultaneously

# Define the output filename, put it in the "Output" subdirectory
output_filename = os.path.join("Output", "Final Report.txt")

# Open the file using "write" mode.
output_file = open(output_filename, 'w')

for line in final_report:

    # Write the line to the text file
    output_file.write (line + "\n")

    # At the same time, print the line to the Terminal Window
    print (line)