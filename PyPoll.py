#The data we need to retrieve
import csv

import os

#Assign a variable to load a file from path.

file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable to save he file to a path.

file_to_save = os.path.join("analysis", "election_analysis.txt")


#1. Initialize a total vote counter

total_votes = 0

#Candidate Options

candidate_options = []

#Candidate Votes

candidate_votes = {}

# Winning Candidate and Winning Count tracker

winning_candidate = ""

winning_count = 0

winning_percentage = 0


#Open the election results and read the file. 

with open(file_to_load) as election_data:

    #To do: Read and Analyze the data here
    file_reader = csv.reader(election_data)

    #Print each row in the CSV File.
    headers = next(file_reader)

    for row in file_reader:
        # Add total vote count
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If statements
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

#Save the results to our text file.

with open(file_to_save, "w") as txt_file:

    #Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    
    print(election_results, end="")

    #Save the final vote count to the text file.

    txt_file.write(election_results)

        #Percentage of votes for each candidate by looping through counts
        #Iterate through candidate list.

    for candidate_name in candidate_votes:

        # Retrieve vote count of candidate

        votes = candidate_votes[candidate_name]

        # Calculate percentage of votes

        vote_percentage = float(votes) / float(total_votes) * 100

        print(f"{candidate_name}: received {vote_percentage}% of the vote.")

        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        print(candidate_results)

        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        #1. Deermine if votes are greater than the winning count. 

        if (votes > winning_count) and (vote_percentage > winning_percentage):

            # 2. If true then set winning count=votes and winning percentage=vote %

            winning_count = votes

            winning_percentage = vote_percentage

            # set winning candidate equal to name

            winning_candidate = candidate_name
    
    # Print winning candidate, vote count and percentage

    #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")


#Print winning candidate results to terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    
    #Save the winning candidate's results to text file
    txt_file.write(winning_candidate_summary)


    
# print(winning_candidate_summary)
    

#1. The total number of votes cast

print(total_votes)

#2. A complete list of candidates who received votes

print(candidate_options)

#3. Total number of votes each candidate received

print(candidate_votes)

#4. Percentage of votes each candidate won


#5. The winner of the election based on popular vote

