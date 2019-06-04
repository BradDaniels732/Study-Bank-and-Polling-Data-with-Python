# Main.py for pybank

# import the modules needed
import os
import csv

# open the csv file
os.chdir(os.path.dirname(__file__))
bank_data_filename = os.path.join ("Resources" , "budget_data.csv")

# Read the csv file and store the data in lists
with open(bank_data_filename, newline='') as bank_file:
    bank_file_reader = csv.reader(bank_file, delimiter=',')

    # Skip the header row
    next(bank_file_reader)

    #initialize the dates and profits lists
    dates = []
    profit = []
    chg_profit = []

    # These variables are used in calculating the chg_profit list
    first_pass = True
    prior_profit = 0

    # Read each row of data after the header
    for row in bank_file_reader:
        dates.append(row[0])
        current_profit = float(row[1])
        profit.append(current_profit)

        # if this is the first pass through this for statement, set the first item in the chg_profit list to zero
        # so that all the lists will be the same length, but keep in mind that there really isn't a "change" 
        # for the first item in the list.  The fact that there is a zero in the first position of the list will
        # not impact further calculations.
        if first_pass:
            chg_profit.append(0)
            first_pass = False
        # this is not the first pass through this for statement, so we can calculate the change from the prior period
        else:
            chg_profit.append(current_profit - prior_profit)

        # Set the prior_profit variable for the next iteration of the for loop
        prior_profit = current_profit


# Calculate the requested data
num_months = len (dates)
total_profit = sum(profit)

# When working with the chg_profit list, start working with the second item in the list, a.k.a. index #1, as that is the 
# first one that has a change.  Recall that the first item in the list, a.k.a. index #0, was set to zero in the "for" loop above.
avg_chg_profit = sum(chg_profit[1:]) / (num_months - 1)
max_chg_profit = max(chg_profit[1:])
min_chg_profit = min(chg_profit[1:])

# Find the dates of the max and min profit
index_max = chg_profit.index(max_chg_profit)
index_min = chg_profit.index(min_chg_profit)

# Put the requested output into a list of strings
final_report = []
final_report.append (f"Financial Analysis")
final_report.append (f"--------------------------")
final_report.append (f"Total months: {num_months}")
final_report.append ("Total Profit: ${0:,.0f}".format(total_profit))
final_report.append ("Average Daily Profit: ${0:,.2f}".format(avg_chg_profit))
final_report.append ("Greatest Increase in Profits:  {0:}  ${1:,.0f}".format(dates[index_max],max_chg_profit))
final_report.append ("Greatest Decrease in Profits:  {0:}  ${1:,.0f}".format(dates[index_min],min_chg_profit))


# Print to a text file and the Terminal Window simultaneously

# Define the output filename, put it in the "Output" subdirectory
output_filename = os.path.join("Output", "Final Report.txt")

# Open the file using "write" mode.
output_file = open(output_filename, 'w')

for line in final_report:

    # Write the line to the text file
    output_file.write (line + "\n")

    # At the same time, print the line to the Terminal Window
    print (line)