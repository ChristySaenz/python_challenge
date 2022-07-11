import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

PL_Values = []
Date = []
PL_Total =[]
# Date formatted as MonthAbv - Year (last 2 numbers)
# Open and read csv
with open(budget_csv) as csvfile:
    csvreader =csv.reader(csvfile, delimiter=",")
    print(csvreader)
    # Read the header row first
    csv_header = next(csvreader) 
    print(f"CSV Header: {csv_header}")
#Calculate Profit/Losses total  
    PL_Total = 0
    for col in csvreader:
        #print(col[1])
        PL_Total += int(col[1])
    print(PL_Total)

        
        

    
  

#Identify the total # of Months
#total_months =  str(len(Date))  
#print("Total Months: " + total_months)
              
#Identify the net_total of Profit/Losses

    
#Find changes in Profit/Losses over the whole period

# Average Profit/Losses Changes

#Identify the greatest increase (Date and amount)

#Identify the greatest decrease (Date and amount)

#Set up print table
#maybe def print_analysis?
#def print_analysis()

   # print("Financial Analysis")
   # print("------------------------------")



# Export results to text file



