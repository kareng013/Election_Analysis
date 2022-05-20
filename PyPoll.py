#The data we need to retrieve
import csv

import os

#Assign a variable to load a file from path.

file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable to save he file to a path.

file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open the election results and read the file. 

with open(file_to_load) as election_data:

    #To do: Read and Analyze the data here
    file_reader = csv.reader(election_data)

    #Print each row in the CSV File.
    headers = next(file_reader)

    print(headers)

#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. Total number of votes each candidate received
#4. Percentage of votes each candidate won
#5. The winner of the election based on popular vote
