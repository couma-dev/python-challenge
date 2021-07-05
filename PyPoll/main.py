
#import dependencies
import csv

#create empty dictionary, this will hold candindates names (key): and candidates votes value:
#create empty list to hold candidates names
#create emptly to hold candidates votes
#set Total vote count to zero (o)
#create empty list to hold winner info
poll_data = {}
Candidates = []
Votes = []
Total_votes_cast = 0
election_winner = []


# set filepath

filepath = "../Resources/election_data.csv"

# open and read the election file.

with open(filepath, 'r') as electioncsv:
    electionreader = csv.reader(electioncsv, delimiter = ',')

    # read the header

    electionheader = next (electioncsv)

    #count total votes cast by iterating through the election data
    for row in electionreader:
        Total_votes_cast +=1

print(Total_votes_cast)


# print election results.
print("Election Results")
print("---------------------------")
print(f"Total Votes: {Total_votes_cast}")
print("---------------------------")
print("")
print()
print()
print()
print("Winner: {}")

#Write election results to output file

