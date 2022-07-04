# The data we need to retrive.
# 1.Total number of votes cast
# 2.Complete list of candidates who received votes
# 3.Percentage of votes each candidate won
# 4.Total number of votes each candidate won
# 5.Winner of the election based on popular vote
import csv

import os

#Assign a variable for the file to load and the path
# file_to_load = 'Resources/election_results.csv'
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file

file_to_save = os.path.join("Analysis", "election_analysis.txt")

# 1.Initialize a total votes counter

total_votes = 0

#setting an open list to add candidate names
candidate_options = []

#Open the election results and read the file

with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    # read the header row
    headers = next(file_reader)

    # print each row in the CSV file

    for row in file_reader:
        # 2. Add to the total vote count
        total_votes += 1

        #Print the dandidate name from each row
        candidate_name = row[2]

        #if statment to see if candidate name has already been added to the candidate list
        if candidate_name not in candidate_options:
            #add the candidate name to the candidate list
            candidate_options.append(candidate_name)

# 3. Print the total votes.
print(f"{total_votes:,}")
print(candidate_options)






#Using the open() function with the "w" mode we will write data to the file.

# with open(file_to_save, "w") as txt_file:
#     txt_file.write("Counties in the Election\n")
#     txt_file.write("-" * 25)
#     txt_file.write ("\nArapahoe\nDenver\nJefferson")
