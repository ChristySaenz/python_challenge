import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

PL_Value = []
PL_Total =[]
Month_Diff = []
Month = []
Fin_Analysis = []
Months = 0
PL_Total = 0
# Open and read csv
with open(budget_csv) as csvfile:
    csvreader =csv.reader(csvfile, delimiter=",")
    # Read the header row first
    csv_header = next(csvreader)  
#Calculate Profit/Losses total  
#Used this stackoverflow thread to adjust code to work for find inc/dec instructions
#https://stackoverflow.com/questions/46965192/python-how-can-i-find-difference-between-two-rows-of-same-column-using-loop-in
    for row in csvreader:
        PL_Value.append(int(row[1]))
#Identify the net_total of Profit/Losses
        PL_Total= sum(PL_Value)
    
#Identify the total # of Months
        Month.append(row[0])
        Months = len(Month)

    Dollar_total = "${:,.2f}".format(PL_Total)

    Fin_Analysis.append("Financial Analysis")
    Fin_Analysis.append("------------------------------")
    Fin_Analysis.append(f"Total Months: {Months}")    
    Fin_Analysis.append(f"Total: {Dollar_total}")
# Setting row count as i by defining the length of the column at each iteration
    for i in range(1, len(PL_Value)):
#Find changes in Profit/Losses over the whole period
# #Subtractracting current row from previous row value
        Month_Diff.append(PL_Value[i]-PL_Value[i-1]) 
# Average Profit/Losses Changes
# #Finding Average change by taking the sum of differences divided by number of months minus due to first month assumed as "no change"
        Avg_Change = "${:,.2f}".format(sum(Month_Diff)/(Months-1))
    Fin_Analysis.append(f"Average Change: {Avg_Change}")
   
# Calculated max and min then idetified value for Month (row [0]) + 1 since the difference needs to start one row down from the first row.
max_diff = None
min_diff = None
for value in Month_Diff:
#Identify the greatest increase (Date and amount) 
    if(max_diff is None or value > max_diff):
        max_diff = value
        max_diff_dol = "${:,.2f}".format(max_diff)
        Max_diff_month = str(Month[Month_Diff.index(max_diff) + 1])
#Identify the greatest decrease (Date and amount)
    if(min_diff is None or value < min_diff): 
        min_diff = value
        min_diff_dol = "${:,.2f}".format(min_diff)
        min_diff_month = str(Month[Month_Diff.index(min_diff) + 1])
Fin_Analysis.append(f"Greatest increase in Profits: {Max_diff_month} ({max_diff_dol})")
Fin_Analysis.append(f"Greatest decrease in Profits: {min_diff_month} ({min_diff_dol})")

#https://www.w3resource.com/python-exercises/list/python-data-type-list-exercise-168.php
#Print each element on own line
for p in Fin_Analysis:
    print(p)

#Export results to text file
Final_Analysis = os.path.join("analysis","Final_Analysis.txt")  
#https://stackoverflow.com/questions/7138686/how-to-write-a-list-to-a-file-with-newlines-in-python3
#With each element on own line
with open(Final_Analysis, mode ="wt") as f:
    for p in Fin_Analysis:
        f.write(p)
        f.write('\n')

    
       


    



