import os
import csv

# Path to collect data from the Resources folder
election_data_csv = os.path.join('Resources', 'election_data.csv')

#Initialize vote count
count_votes = 0
candidate1_vote_count = 0
candidate2_vote_count = 0
candidate3_vote_count = 0
percentage1 = 0
percentage2 = 0
percentage3 = 0
vote_array = []
unique_candidate_list = []

# Define function that accepts 'election_analysis_data' as parameter
def print_stats(election_analysis_data):
    global vote_array
    vote = str(election_analysis_data[2])
    vote_array.append(vote)


#Read in the CSV file
with open(election_data_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)


    # Loop through the data
    for row in csvreader:

        # Increment count_votes for each row
        count_votes = count_votes + 1
        print_stats(row)
   

print("-------------------------------")
print("Election Results")
print("-------------------------------")

# Print out the month count
print(f"Total Votes: {count_votes}")
print("-------------------------------")


for x in vote_array:
    #check if list entry is unique or not
    if x not in unique_candidate_list:
            unique_candidate_list.append(x)


for y in vote_array:
    if y == unique_candidate_list[0]:
        candidate1_vote_count = candidate1_vote_count + 1
    elif y == unique_candidate_list[1]:
         candidate2_vote_count = candidate2_vote_count + 1
    elif y == unique_candidate_list[2]:
         candidate3_vote_count = candidate3_vote_count + 1
    
vote_count_list = [candidate1_vote_count, candidate2_vote_count, candidate3_vote_count]

percentage1 = (candidate1_vote_count/count_votes) * 100
percentage2 = (candidate2_vote_count/count_votes) * 100
percentage3 = (candidate3_vote_count/count_votes) * 100

# Round the percentage to 3 decimal places
percentage_rounded_number1 = round(percentage1, 3)
percentage_rounded_number2 = round(percentage2, 3)
percentage_rounded_number3 = round(percentage3, 3)

percentage_list = [percentage_rounded_number1, percentage_rounded_number2, percentage_rounded_number3]


for i in range(len(unique_candidate_list)):
    print(f"{unique_candidate_list[i]}: {percentage_list[i]}% ({vote_count_list[i]})")
    results_list = [unique_candidate_list[i], percentage_list[i], vote_count_list[i]]
    

max_votes = max(vote_count_list)

for j in range(len(unique_candidate_list)):
    if vote_count_list[j] == max(vote_count_list):
        print("-------------------------------")
        print(f"Winner: {unique_candidate_list[j]}")
        print("-------------------------------")