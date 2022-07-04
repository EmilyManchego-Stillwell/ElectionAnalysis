#add dependencies
import csv

import os

#assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

#assign a variable to save the file to a path
file_to_save = os.path.join("Analysis", "election_results.txt")

#initialize a total votes counter
total_votes = 0

#creating an empty list to add counties
counties = []

#creating an empty dictionary to show county names with total votes
county_votes = {}

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
        #add to the total vote count
        total_votes += 1

        #get the candidate name from each row
        candidate_name = row[2]

        #if statment to see if candidate name has already been added to the candidate list
        if candidate_name not in candidate_options:
            #add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            #initializing key for candidate_votes dictionary & begin tracking candidate's vote count
            candidate_votes[candidate_name] = 0

        #add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        #get the county name from each row
        county_name = row[1]
        
        #if statement to see if county name has already been added to the list
        if county_name not in counties:
            counties.append(county_name)
            county_votes[county_name] = 0
        county_votes[county_name] += 1
        
#save the results to a text file
with open(file_to_save, "w") as txt_file:
    #will print the final vote count to the terminal
    election_results = (
        f"Election Results\n"
        +"-"*25 + "\n"
        f"Total Votes: {total_votes:,}\n"
        +"-"*25 + "\n"
    )
    print(election_results, end="")

    #save the final vote count to the text file
    txt_file.write(election_results)

    #determine the percentage of votes for each candidate
    for candidate_name in candidate_votes:
        #retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        
        vote_percentage = ((votes/total_votes)*100)

        #create a variable to print each candidate's results
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        print(candidate_results)
        #save the individual candidate results to the txt file
        txt_file.write(candidate_results)
        
        #determine winning vote count and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            
            winning_count = votes

            winning_percentage = vote_percentage
            
            winning_candidate = candidate_name

    #will print the winning candidate's results to the terminal
    winning_candidate_summary = (
        f"---------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}\n"
        f"---------------------------\n"
    )

    print(winning_candidate_summary)
    #save the candidate summary to the txt file
    txt_file.write(winning_candidate_summary)

    #list each county on its own row with the total number of votes per county. 
    #list each county showing the percentage of votes for each county
    #list the county with the highest turnout stating number of voters and percentage of voters

    #County Results
    # -------------------------
    # Arapahoe: county_vote_percentage% (county_votes)
    # Denver: county_vote_percentage% (county_votes)
    # Jefferson: county_vote_percentage% (county_votes)
    # ---------------------------
    # County with Highest Turnout: county_name
    # Vote Count for County with Highest Turnout: county_votes
    # Highest County Voter Turnout Percentage: 73.8
    # ---------------------------
    