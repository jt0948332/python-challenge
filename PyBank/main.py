import csv
import os

# Containers
BudgetData = os.path.join("Resources", "budget_data.csv")
# read the file

net_profit = 0.0
row_count = 0
prev_value = None
change_list = []

min_change = 0
max_change = 0
min_change_month = None
max_change_month = None

with open(BudgetData) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)
    for row in csv_reader:
        current_value = int(row[1])
        current_month = row[0]
        # Calculate Change from Month to Month
        if prev_value:
            change = current_value - prev_value
            change_list.append(change)
            if int(change) > int(max_change):
                max_change = change
                max_change_month = row[0]
            if int(change) < int(min_change):
                min_change = change
                min_change_month = row[0]
                #changeList.append(Date1)
        prev_value = current_value
        # Count number of Rows
        row_count += 1
        #  Calculate Total
        net_profit += current_value

average_change = round(((sum(change_list))/len(change_list)), 2)
#print everything out
print("Financial Analysis")
print("--------------------------------------------")
print(f"Total Months: {row_count}")
print(f"Total: ${net_profit}")
print(f"Average Change: $ {average_change}")
print(f"Greatest Increase in Profits: {max_change_month} (${max_change})")
print(f"Greatest Decrease in Profits: {min_change_month} (${min_change})")

#Write to file
output_path = os.path.join("Resources", "output.csv")
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Total Months', 'Total', 'Average Change','Greatest increase in Profits', 'Greatest Decrease in Profits'])


    # Write the second row
    csvwriter.writerow([row_count, net_profit, average_change, max_change_month + " $" +  str(max_change), min_change_month + " $" + str(min_change)])
#print(f"Total Months: {row_count} received {tally_percent} % ({tally_count})")