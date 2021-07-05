import csv


import csv

#create empty lists and and dictionaries assign to variables to store our calculations.

poll_data = {}
Candidates = []
Votes = []
Total_votes_cast = 0


# set filepath

filepath = "../Resources/election_data.csv"

# open and read the election file.

with open(filepath, 'r') as electioncsv:
    electionreader = csv.reader(electioncsv, delimiter = ',')

    # read the header

    electionheader = next (electioncsv)

    #count total votes cast 
    for row in electionreader:
        Total_votes_cast +=1

print(Total_votes_cast)

