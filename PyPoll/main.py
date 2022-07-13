import os
import csv

elec_csv = os.path.join("Resources", "election_data.csv")
Voters = []
County = []
U_Counties = []
Canidate = []
U_Canidates = []
CCS_Votes = 0
DDG_Votes = 0
RAD_Votes = 0
# three columns: "Voter ID", "County", and "Candidate"
with open(elec_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader) 
# The total number of votes cast
    for row in csvreader:
        Voters.append(int(row[0]))
        County.append(row[1])
        Canidate.append(row[2])
    total_votes = len(Voters)    
    for c in Canidate:
        if c not in U_Canidates:
            U_Canidates.append(c)  
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
# A complete list of candidates who received votes
print([U_Canidates])
# The percentage of votes each candidate won
for v in Canidate:
    if v == "Charles Casper Stockham":
        CCS_Votes = CCS_Votes + 1
    if v == "Diana DeGette":
        DDG_Votes =DDG_Votes + 1
    if v == "Raymon Anthony Doane":
        RAD_Votes =RAD_Votes + 1
per_votes_CCS = (CCS_Votes/total_votes) * 100
per_votes_DDG = (DDG_Votes/total_votes) * 100
per_votes_RAD = (RAD_Votes/total_votes) * 100
# The total number of votes each candidate won
print(f"CCS Votes: {per_votes_CCS} ({CCS_Votes})")
print(f"DDG Votes: {per_votes_DDG} ({DDG_Votes})")
print(f"RAD Votes: {per_votes_RAD} ({RAD_Votes})")
# The winner of the election based on popular vote.