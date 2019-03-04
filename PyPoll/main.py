import csv
import os
total_votes = 0
candidate_list = []
all_votes = []
row2 = []
final_tally= {}
winner_count = 0
winner = []
output = []

# Containers
PollData = os.path.join("Resources", 'election_data.csv')
# read the file
with open(PollData) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)
    for row in csv_reader:
        #count total number of votes
        total_votes += 1
        all_votes.append(row[2])

        # create unique candidates list - Use to loop through and count later
        if row[2] not in candidate_list:
            candidate_list.append(row[2])

        #count the different occurences
            # add all row2 to dictionary
            row2.append(row[2])

print(f"Total Votes:: {total_votes}")
print("--------------------------------------------")
#Do all the tallying
candidates: object
for candidates in candidate_list:
    tally_count = (all_votes.count(candidates))
    if tally_count > winner_count:
        winner_count = tally_count
        winner = candidates
    tally_percent = round(((tally_count/total_votes)*100))
    print(f"Candidate: {candidates} received {tally_percent} % ({tally_count})")
    #attach to variable
    output.append(f"Candidate: {candidates} received {tally_percent} % ({tally_count})")
    # Attach to variable
    #output.append([candidates, tally_percent, tally_count])

print("--------------------------------------------")
print(f"Winner: {winner}")
print("--------------------------------------------")
#Write to file
output_path = os.path.join("Resources", "poll_output.csv")
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Total Votes Counted', 'Details by Candidate', 'The winner is'])


    # Write the second row
    csvwriter.writerow([tally_count, output, winner])
#print(f"Total Months: {row_count} received {tally_percent} % ({tally_count})")
