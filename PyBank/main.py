import os
import csv

# Path to collect data from the Resources folder
budget_data_csv = os.path.join('Resources', 'budget_data.csv')

#Initialize month count
count_month = 0
total = 0
profit_loss = 0
profit_loss_array = []
date_array = []
profit_loss_change = 0
#profit_loss_change_total = 0
profit_loss_change_array = []
sum_changes = 0
rounded_number = 0
max_change = 0
min_change = 0

# Define function that accepts 'financial_analysis_data' as parameter
def print_stats(financial_analysis_data):
    global profit_loss
    global profit_loss_array 
    global date_array
    #global profit_loss_change
    date = str(financial_analysis_data[0])
    date_array.append(date)
    profit_loss = int(financial_analysis_data[1])
    profit_loss_array.append(profit_loss)

 
#Read in the CSV file
with open(budget_data_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)


        # Loop through the data
    for row in csvreader:

        # Increment count_month for each row
        count_month = count_month + 1
        print_stats(row)
        total += int(row[1])
       

print("-------------------------------")
print("Financial Analysis")
print("-------------------------------")

# Print out the month count
print(f"Total Months: {count_month}")
print(f"Total: ${total}")


# Create list for monthly changes
for i in range(len(profit_loss_array)):
    #If statement to avoid Index out of range error
    if i < ((len(profit_loss_array)) - 1):
        profit_loss_change = profit_loss_array[i+1] -profit_loss_array[i]
        profit_loss_change_array.append(profit_loss_change)

max_change = max(profit_loss_change_array)
min_change = min(profit_loss_change_array)


# Calculate average change
sum_changes = sum(profit_loss_change_array)/len(profit_loss_change_array)
rounded_number = round(sum_changes, 2)
print(f"Average Change: ${rounded_number}")

# Get the greatest increases and decreases for all months
for j in range(len(profit_loss_change_array)):
    if profit_loss_change_array[j] == max(profit_loss_change_array):
        print(f"Greatest increase Month: {date_array[j+1]} ($ {max_change})")
        inc_month = date_array[j+1]
    elif profit_loss_change_array[j] == min(profit_loss_change_array):
        print(f"Greatest decrease Month: {date_array[j+1]} ($ {min_change})")
        decr_month = date_array[j+1]

print("-------------------------------")            


# Writeto text file /Analyses/results.txt
results_path = os.path.join('Analyses', 'results.txt')
results = open(results_path, "w")
results.write('Total Months: ' + str(count_month) + '\n')
results.write('Total: $' + str(total) + '\n')
results.write('Average Change: $' + str(rounded_number) + '\n')
results.write('Greatest Increase: ' + str(inc_month) + ' ($' + str(max_change) + ')' + '\n')
results.write('Greatest Decrease: ' +str(decr_month) + ' ($' + str(min_change) + ')' + '\n')
results.close()