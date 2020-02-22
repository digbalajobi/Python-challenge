import os

import csv

csvpath = os.path.join('budget_data.csv')

#lists

total_months = 0
nettotal_profit_loss = 0
orig_profit_loss = 0
avg_change_PL = 0


with open(csvpath, newline='') as budgetdata:

    csvreader = csv.reader(budgetdata, delimiter=",")

    print(csvreader) 
    
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")


    # Read  data after the header
    for row in csvreader:
       
     
        #The total number of months included in the dataset

        total_months = total_months + 1

        #The net total amount of "Profit/Losses" over the entire period

        nettotal_profit_loss = nettotal_profit_loss + int(row[1])

        #The average of the changes in "Profit/Losses" over the entire period

        if total_months > 1:
            avg_change_PL = int(row[1]) - orig_profit_loss



    print ( "Total # of Months: " + str(total_months))
    print ("Total Amount of Profit/Losses: $" + str(nettotal_profit_loss))
    print ("Avg. Change in Profit/Losses: $" + str(avg_change_PL ))

