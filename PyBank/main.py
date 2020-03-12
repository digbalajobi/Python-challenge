#importing data

import os

import csv

csvpath = os.path.join('budget_data.csv')
PyBank_output = ('PyBank.txt')


#lists

total_months = 0
nettotal_profit_loss = 0
orig_profit_loss = 0

net_change_list = []
month_change_list = []

#creating a list to capture greatest increase and decrease in profit/losses and the month

greatest_increase = ["",0]
greatest_decrease = ["", 99999999999999999999]

#opening and reading in data 

with open(csvpath, newline='') as budgetdata:

    csvreader = csv.reader(budgetdata, delimiter=",")

    print(csvreader) 
    
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #setting up data in the initial row

    firstrow = next(csvreader)
    total_months = total_months + 1
    nettotal_profit_loss = nettotal_profit_loss + int(firstrow[1])
    orig_profit_loss = int(firstrow[1])

    # Read  data after the header
    for row in csvreader:

        #The total number of months included in the dataset

        total_months = total_months + 1

        #The net total amount of "Profit/Losses" over the entire period


        nettotal_profit_loss = nettotal_profit_loss + int(row[1])

        #The average of the changes in "Profit/Losses" over the entire period

        net_change = int(row[1]) - orig_profit_loss

        #-----------------------------------------------------------------------------

        net_change_list = net_change_list + [net_change]
        month_change_list = month_change_list + [row[0]]


        #checking for greatest increase
        #The greatest increase in profits (date and amount) over the entire period
        

        if net_change > greatest_increase[1]:
                greatest_increase[0] = row[0]

                greatest_increase[1] = net_change
            

        #The greatest decrease in losses (date and amount) over the entire period

        if net_change < greatest_decrease[1]:
                greatest_decrease[0] = row[0]

                greatest_decrease[1] = net_change
            

        orig_profit_loss = int(row[1]) 

average_monthly_net_change = sum(net_change_list) / len(month_change_list)
  
print("Financial Analysis")
print("-----------------------------------")
print( "Total Months: " + str(total_months)
print("Total: $" + str(nettotal_profit_loss)
print("Avg. Change in Profit/Losses: $" + str(average_monthly_net_change )
print("Greatest Increase in Profit: " + str(greatest_increase[0]) + " / " + "$" + str(greatest_increase[1])
print("Greatest Decrease in Profit: " + str(greatest_decrease[0]) + " / " + "$" + str(greatest_decrease[1]) 

with open(PyBank_output, "w", newline='') as textfile:
        print("Financial Analysis", file=textfile)
        print("-----------------------------------", file=textfile)
        print( "Total Months: " + str(total_months), file=textfile)
        print("Total: $" + str(nettotal_profit_loss), file=textfile)
        print("Avg. Change in Profit/Losses: $" + str(average_monthly_net_change ), file=textfile)
        print("Greatest Increase in Profit: " + str(greatest_increase[0]) + " / " + "$" + str(greatest_increase[1]), file=textfile) 
        print("Greatest Decrease in Profit: " + str(greatest_decrease[0]) + " / " + "$" + str(greatest_decrease[1]), file=textfile) 

