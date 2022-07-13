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
per_votes = []
election_results = []
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
election_results.append("Election Results")
election_results.append("-------------------------")
election_results.append(f"Total Votes: {total_votes}")
# A complete list of candidates who received votes
#print(U_Canidates)
# The percentage of votes each candidate won
for v in Canidate:
    if v == "Charles Casper Stockham":
        CCS_Votes = CCS_Votes + 1
    if v == "Diana DeGette":
        DDG_Votes =DDG_Votes + 1
    if v == "Raymon Anthony Doane":
        RAD_Votes =RAD_Votes + 1
per_votes_CCS = "{0:.3f}%".format((CCS_Votes/total_votes) * 100)
per_votes_DDG = "{0:.3f}%".format((DDG_Votes/total_votes) * 100)
per_votes_RAD = "{0:.3f}%".format((RAD_Votes/total_votes) * 100)
# The total number of votes each candidate won
election_results.append("-------------------------")
election_results.append(f"Charles Casper Stockham: {per_votes_CCS} ({CCS_Votes})")
election_results.append(f"Diana DeGette: {per_votes_DDG} ({DDG_Votes})")
election_results.append(f"Raymon Anthony Doane: {per_votes_RAD} ({RAD_Votes})")
election_results.append("-------------------------")
# The winner of the election based on popular vote.
# per_votes = [per_votes_CCS, per_votes_DDG, per_votes_RAD]
# print(per_votes)
#Winner = None
election_results.append("Winner: ")
election_results.append("-------------------------")

for p in election_results:
    print(p)

#Export results to text file
fin_elec_results = os.path.join("analysis","Final_Results.txt")  
#https://stackoverflow.com/questions/7138686/how-to-write-a-list-to-a-file-with-newlines-in-python3
with open(fin_elec_results, mode ="wt") as f:
    for p in election_results:
        f.write(p)
        f.write('\n')
