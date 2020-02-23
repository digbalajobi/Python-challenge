#importing data

import os

import csv

csvpath = os.path.join('election_data.csv')
PyPoll_output = ('PyPoll.txt')



#Lists

total_votes = 0 
total_candidates = 0
candidate = []
results = []
votes = []
percentage = []

#opening and reading in data 

with open(csvpath, newline='') as electiondata:

    csvreader = csv.reader(electiondata, delimiter=",")

    print(csvreader) 
    
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:

        #The total number of votes cast

        total_votes = total_votes + 1

        #A complete list of candidates who received votes

        candidate.append(row[2])

for i in set (candidate):
    results.append(i)
    votes.append(candidate.count(i))
            #The percentage of votes each candidate won

    percentage.append((candidate.count(i)/total_votes)*100)

    total_candidates = total_candidates + 1

        #The winner of the election based on popular vote.

    winner = results[votes.index(max(votes))]


with open(PyPoll_output, "w", newline='') as textfile:

    print ("Election Results ", file=textfile)
    print("-----------------------------------", file=textfile)

    print ( "Total Votes: " + str(total_votes), file=textfile)
    print("-----------------------------------", file=textfile)

    for i in range(total_candidates):
        print(f'{results[i]}: {round(percentage[i], 2)}% ({votes[i]})', file=textfile)
    print("-----------------------------------", file=textfile)

    print(f'Winner: {winner}', file=textfile)
    print("-----------------------------------", file=textfile)

