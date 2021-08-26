import os
import csv

# Create voting total variables
total_votes = 0
Khan_votes = 0
Correy_votes = 0
Li_votes = 0
O_Tooley_votes = 0
# Create dictionary which contains the percentage of the total vote won by each candidate
election_votes_percent_dict = {}

election_path = os.path.join("Resources", "election_data.csv")

with open(election_path) as election_file:
    csv_reader = csv.reader(election_file)
    # Get the headers
    next(csv_reader)
    for row in csv_reader:
        # Get the total number of votes
        total_votes += 1
        if (row[2] == "Khan"):
            Khan_votes += 1
        elif (row[2] == "Correy"):
            Correy_votes += 1
        elif (row[2] == "Li"):
            Li_votes += 1
        else:
            O_Tooley_votes += 1
        
# Find each candidate's percentage of the total vote and add it to a dictionary
election_votes_percent_dict["Khan"] = round((Khan_votes/total_votes)*100,3)
election_votes_percent_dict["Correy"] = round((Correy_votes/total_votes)*100,3)
election_votes_percent_dict["Li"] = round((Li_votes/total_votes)*100,3)
election_votes_percent_dict["O'Tooley"] = round((O_Tooley_votes/total_votes)*100,3)

# Find the winner
winner = max(election_votes_percent_dict, key=election_votes_percent_dict.get)

# Create an output list
election_results_list = [
    "Election Results",
    "-------------------------",
    f"Total Votes: {total_votes}",
    "-------------------------",
    f"Khan: {election_votes_percent_dict['Khan']}%  ({Khan_votes})",
    f"Correy: {election_votes_percent_dict['Correy']}% ({Correy_votes})",
    f"Li: {election_votes_percent_dict['Li']}% ({Li_votes})",
    "O'Tooley: " + str(election_votes_percent_dict["O'Tooley"]) + f"% ({O_Tooley_votes})",
    "-------------------------",
    f"Winner: {winner}",
    "-------------------------"
]

# Print the result to the terminal
for line in  election_results_list: print(line)

# Export the result
output_path = os.path.join("analysis", "election_analysis_results.txt") # Specify the file path to write to
with open(output_path, 'w') as text_file: # Open the file using "write" mode and write the output
        text_file.write('\n'.join(election_results_list))