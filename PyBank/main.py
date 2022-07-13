import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

PL_Value = []
PL_Total =[]
Month_Diff = []
Month = []
# Date formatted as MonthAbv - Year (last 2 numbers)
# Open and read csv
Months = 0
PL_Total = 0
with open(budget_csv) as csvfile:
    csvreader =csv.reader(csvfile, delimiter=",")
    #print(csvreader)
    # Read the header row first
    csv_header = next(csvreader) 
    #print(f"CSV Header: {csv_header}") 
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

    print("Financial Analysis")
    print("------------------------------")
    print (f"Total Months: {Months}")    
    print(f"Total: {Dollar_total}")
# Setting row count as i by defining the length of the column at each iteration
    for i in range(1, len(PL_Value)):
#Find changes in Profit/Losses over the whole period
# #Subtractracting current row from previous row value
        Month_Diff.append(PL_Value[i]-PL_Value[i-1]) 
# Average Profit/Losses Changes
# #Finding Average change by taking the sum of differences divided by number of months minus due to first month assumed as "no change"
        Avg_Change = "${:,.2f}".format(sum(Month_Diff)/(Months-1))
    #print (f"{i} : {Month_Diff}")
    print(f"Average Change: {Avg_Change}")
   
#Identify the greatest increase (Date and amount)
#https://www.delftstack.com/howto/python/python-max-value-in-list/
# pos_pl_value = []
# neg_pl_value = []
# for x in PL_Value:
#     if (x >= 0):
#         pos_pl_value.append(x)
#     else:
#         neg_pl_value.append(x)
#     print(max(pos_pl_value))
#     print(max(neg_pl_value))
#Identify the greatest decrease (Date and amount)
max_diff = None
min_diff = None
for value in Month_Diff: 
    if(max_diff is None or value > max_diff):
        max_diff = value
        max_diff_dol = "${:,.2f}".format(max_diff)
        Max_diff_month = str(Month[Month_Diff.index(max_diff)])
    if(min_diff is None or value < min_diff): 
        min_diff = value
        min_diff_dol = "${:,.2f}".format(min_diff)
        min_diff_month = str(Month[Month_Diff.index(min_diff) + 1])
print(f"Greatest increase in Profits: {Max_diff_month} ({max_diff_dol})")
print(f"Greatest decrease in Profits: {min_diff_month} ({min_diff_dol})")

#Set up print table

# Export results to text file



