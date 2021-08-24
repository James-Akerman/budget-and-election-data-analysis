import os
import csv

budget_path = os.path.join("Resources", "budget_data.csv")
total_months = 0
net_profit = 0
monthly_change_dictionary = {}
previous_budget = 0
monthly_change = 0
average_change = 0

with open(budget_path) as budget_file:
    csv_reader = csv.reader(budget_file)    
    # Get the headers
    next(csv_reader)
    #Get all the dates
    for row in csv_reader:
        #Get the monthly change
        if previous_budget != 0:
            current_month = row[0]
            current_budget = int(row[1])
            monthly_change = current_budget - previous_budget
            monthly_change_dictionary[current_month] = monthly_change
            previous_budget = current_budget
            previous_month = current_month
        else:
            previous_month = row[0]
            previous_budget = int(row[1])
        # Get the total number of months
        total_months += 1
        # Get the net profit/loss
        net_profit += int(row[1])

# Get the average monthly change
    for k,v in monthly_change_dictionary.items():
        average_change+=v  
average_change = round(average_change/len(monthly_change_dictionary),2)

# Which month had the greatest increase
greatest_increase = max(monthly_change_dictionary, key=monthly_change_dictionary.get)

# Which month had the greatest decrease
greatest_decrease = min(monthly_change_dictionary, key=monthly_change_dictionary.get)

# Create an output list
budget_results_list = ["Financial Analysis",
    "----------------------------",
    f"Total Months: {total_months}",
    f"Total: ${net_profit}",
    f"Average Change: ${average_change}",
    f"Greatest Increase in Profits: {greatest_increase} (${monthly_change_dictionary[greatest_increase]})",
    f"Greatest Decrease in Profits: {greatest_decrease} (${monthly_change_dictionary[greatest_decrease]})"
    ]
    
# Print the result to the terminal
for i in budget_results_list: print(i)

# Export the result
output_path = os.path.join("analysis", "budget_analysis_results.txt") # Specify the file path to write to
with open(output_path, 'w') as text_file: # Open the file using "write" mode and write the output
        text_file.write('\n'.join(budget_results_list))