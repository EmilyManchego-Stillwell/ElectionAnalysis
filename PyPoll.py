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

#Open the election results and read the file

with open(file_to_load) as election_data:
    
    # To do : read and analyze data here
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # print the header row
    headers = next(file_reader)

    print(headers)

    # print each row in the CSV file

    # for row in file_reader:
    #     print(row)




#Using the open() function with the "w" mode we will write data to the file.

# with open(file_to_save, "w") as txt_file:
#     txt_file.write("Counties in the Election\n")
#     txt_file.write("-" * 25)
#     txt_file.write ("\nArapahoe\nDenver\nJefferson")
