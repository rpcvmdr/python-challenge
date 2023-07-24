import os
import csv

# Commands to load budget_data.csv file and to create a location to output an analysis text file
budgetcsv = os.path.join("Resources", "budget_data.csv")
analysis_output = os.path.join("analysis", "analysis_budget_data.txt")

# Commands to create and track several financial parameters
total_months = 0
net_total = 0
month_of_change = []
list_net_change = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

# Commands to read the csv file, convert it into list of dictionaries and clarify the character that separates \n
# the columns 
with open(budgetcsv, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Read the first/header row and extract it to avoid adding it to calculations
    csvheader = next(csvreader)
    first_row = next(csvreader)  
    total_months = total_months + 1
    net_total = net_total + int(first_row[1])
    prev_net = int(first_row[1])
 
    # Commands to read each month of data to track totals
    for row in csvreader:
        total_months += 1
        net_total += int(row[1])

        # Commands to calculate the net changes in profits       
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        list_net_change += [net_change]
        month_of_change += [row[0]]

        # Commands to calculate the greatest increase in profits
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        # Commands to calculate the greatest decrease in profits
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

    # Calculate the Average Net Change 
    Monthy_Average_Net = sum(list_net_change) / len(list_net_change)

# Prepare Output Summary with key categories and print to the terminal
output = (f"Financial Analysis\n"
          f"------------------------------\n"
          f"Total Months:  {total_months}\n"
          f"Total:  ${net_total:0,.0f}\n"
          f"Average Change: ${Monthy_Average_Net:0,.2f}\n"
          f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]:0,.0f})\n"
          f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]:0,.0f})\n")                  
print(output)

# Command to export the above output summary as a text file
with open(analysis_output, "w") as txt_file:
        txt_file.write(output)
