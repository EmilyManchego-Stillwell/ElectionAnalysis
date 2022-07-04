# The data we need to retrive.
# 1.Total number of votes cast
# 2.Complete list of candidates who received votes
# 3.Percentage of votes each candidate won
# 4.Total number of votes each candidate won
# 5.Winner of the election based on popular vote

#add dependencies
import csv

import os

#assign a variable to load a file from a path.
# file_to_load = 'Resources/election_results.csv'
file_to_load = os.path.join("Resources", "election_results.csv")

#assign a variable to save the file to a path

file_to_save = os.path.join("Analysis", "election_analysis.txt")

#initialize a total votes counter

total_votes = 0

#creating an empty list to add candidate names
candidate_options = []

#creating an empty dictionary to show candidate name with total votes

candidate_votes = {}

#winning candidate and winning count tracker

winning_candidate = ""

winning_count = 0

winning_percentage = 0

#open the election results and read the file

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

            #initializing key for candidate_votes dictionary & begin tracking candidate's vote count
            candidate_votes[candidate_name] = 0

        #add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

#determine the percentage of votes for each candidate
for candidate_name in candidate_votes:
    #retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]
    #calculate the percentage of votes
    vote_percentage = ((votes/total_votes)*100)

    #to do: print out each candidate's name, vote count, and percentage of votes to the terminal
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    #determine winning vote count and candidate
    #determine if the votes are greater than winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #if true set winning_count = votes & winning_percentage = vote_percentage
        winning_count = votes

        winning_percentage = vote_percentage
        #set winning_candidate equal to the candiate's name
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"---------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}\n"
    f"---------------------------\n"
)

print(winning_candidate_summary)

    # print(f"{winning_candidate} is the winning candidate. {winning_candidate} got {votes:,} votes and had {winning_percentage:.f1}% 
    # of the total votes.")

    #print(f"{candidate_name} got {votes:,} votes.")
    # print(f"{candidate_name} got {vote_percentage:.1f}% of the total votes.")
    #this is where we print the candidate vote dictionary
    # print(f"{total_votes:,}")
    # print(candidate_options)
    # print(candidate_votes)






#Using the open() function with the "w" mode we will write data to the file.

# with open(file_to_save, "w") as txt_file:
#     txt_file.write("Counties in the Election\n")
#     txt_file.write("-" * 25)
#     txt_file.write ("\nArapahoe\nDenver\nJefferson")
