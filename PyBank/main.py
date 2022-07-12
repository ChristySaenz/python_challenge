import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

PL_Value = []
PL_Total =[]
Month_Diff = []
# Date formatted as MonthAbv - Year (last 2 numbers)
# Open and read csv
Months = 0
PL_Total = 0
with open(budget_csv) as csvfile:
    csvreader =csv.reader(csvfile, delimiter=",")
    #print(csvreader)
    # Read the header row first
    csv_header = next(csvreader) 
    print(f"CSV Header: {csv_header}") 
#Calculate Profit/Losses total  
    for row in csvreader:
        PL_Value.append(int(row[1]))
#Identify the net_total of Profit/Losses
        PL_Total= sum(PL_Value)
    
#Identify the total # of Months
        Months += 1
    Dollar_total = "${:,.2f}".format(PL_Total)
#https://stackoverflow.com/questions/46965192/python-how-can-i-find-difference-between-two-rows-of-same-column-using-loop-in
       
    print("Financial Analysis")
    print("------------------------------")
    print (f"Total Months: {Months}")    
    print(f"Total: {Dollar_total}")
# Setting row count as i by defining the length of the column at each iteration
    for i in range(1, len(PL_Value)):
#Subtractracting current row from previous row value
        Month_Diff.append(PL_Value[i]-PL_Value[i-1]) 
#Finding Average change by taking the sum of differences divided by number of months minus due to first month assumed as "no change"
        Avg_Change = "${:,.2f}".format(sum(Month_Diff)/(Months-1))
    #print (Month_Diff)
    print(f"Average Change: {Avg_Change}")
   
        
    

    


       

              


    
#Find changes in Profit/Losses over the whole period

# Average Profit/Losses Changes

#Identify the greatest increase (Date and amount)

#Identify the greatest decrease (Date and amount)

#Set up print table
#maybe def print_analysis?
#def print_analysis()

   



# Export results to text file



