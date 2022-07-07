import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

#Lists to store data

Profit_Loss_Value = []

# Open and read csv
with open(budget_csv) as csv_file:
    csvreader =csv.reader(csv_file, delimiter=",")

    # Read the header row first
    csv_header = next(csv_file)
    #print(f"Header: {csv_header}")
    # Date formatted as MonthAbv - Year (last 2 numbers)
    Date = [row[0] for row in csvreader]
    Profit_Loss_Value = [row[1] for row in csvreader]
    #for row in csvreader:
        #Date.append(row[0])
        #Profit_Loss_Value.append(row[1])

#Identify the total # of Months
total_months =  str(len(Date))  
print("Total Months: " + total_months)
              
#Identify the net_total of Profit/Losses

#def pl_average(Profit_Loss_Value)
        #Profit_Loss_Value =int()
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



