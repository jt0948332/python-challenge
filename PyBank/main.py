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

print(net_profit)
print(row_count)
print((sum(change_list))/len(change_list))
print(min(change_list))
print(max_change_month)
print(max_change)
print(min_change_month)
print(min_change)
