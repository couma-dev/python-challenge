
#import dependencies
import csv

#create empty dictionary, this will hold candindates names (key): and candidates votes value:
#create empty list to hold candidates names
#create emptly to hold candidates votes
#set Total vote count to zero (o)
#create empty list to hold winner info
#create empty list to hold vote percentage
poll_data = {}
Candidates = []
Votes = []
Total_votes_cast = 0
Votes_percentage = []
election_winner = []


# set filepath

filepath = "../Resources/election_data.csv"

# open and read the election file.

with open(filepath, 'r') as electioncsv:
    electionreader = csv.reader(electioncsv, delimiter = ',')

    # read the header

    electionheader = next (electioncsv)

    # 1. count total votes cast by iterating through the election data
    #2. iterate through the tuple created by accessing the column 3 keys (candindate names) in the poll_data dictionary, picking candidate name only once
    for row in electionreader:
        Total_votes_cast +=1
        if row[2] in poll_data.keys():
            poll_data[row[2]] = poll_data[row[2]] + 1
        else: poll_data[row[2]] = 1

# fill the candiate and their respective votes from the poll_data dictionary into the emply lists created above.
#use .item function to access their whole dictionary

for k, v in poll_data.items():
    Candidates.append(k)
    Votes.append(v)
# loop through the votes list and create the vote percentage based on the total votes cast
for i in Votes:
     Votes_percentage.append(round(i/Total_votes_cast*100,2))

# votes per candidates, candidates and their respective votes into a new tuple
final_vote_tally = list(zip(Candidates,Votes,Votes_percentage))

# iterate through the finaal votes tally  tuple & create the election winners list by determining the highest vote in votes column

for name in final_vote_tally:
    if max(Votes) == name[1]:
        election_winner.append(name[0])
#election winner is first entry on the election winners list
winner = election_winner[0]


# print election results.
print("Election Results")
print("---------------------------")
print(f"Total Votes: {Total_votes_cast}")
print("---------------------------")
for (c,vp,v) in zip (Candidates,Votes_percentage,Votes):
    print(f"{c}: {vp}% ({v})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")

#Write election results to output file

electionoutput_filepath = "../Analysis/ElectionAnalysis.txt"
with open(electionoutput_filepath, 'w') as ElectionAnalysistxt:
    ElectionAnalysistxt.write("Election Results\n")
    ElectionAnalysistxt.write("---------------------------\n")
    ElectionAnalysistxt.write(f"Total Votes: {Total_votes_cast}\n")
    ElectionAnalysistxt.write("---------------------------\n")
    for (c,vp,v) in zip (Candidates,Votes_percentage,Votes):
        ElectionAnalysistxt.write(f"{c}: {vp}% ({v})\n")
    ElectionAnalysistxt.write("---------------------------\n")
    ElectionAnalysistxt.write(f"Winner: {winner}\n")
    ElectionAnalysistxt.write("---------------------------")
