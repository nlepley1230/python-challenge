#import packages
import csv
import os

#function to fix percentage format to 3 decimal points
def fixPercent(num):
    num = "{:.3%}".format(num)
    return num

#define relative path for the input and output files ---
inputfile = os.path.join("Resources", "election_data.csv")
outputfile = os.path.join("analysis", "pyPoll_analysis.txt")

#empty lists and variables
Unique_Candidates = []
Vote_Counts = []
Vote_Percent = []
Total_Votes = 0
Winner_Count = 0

#read the CSV file
with open(inputfile, 'r') as electiondata:
    election_reader = csv.reader(electiondata, delimiter=",")

    Headers = next(election_reader)

    for row in election_reader:
        Total_Votes += 1
    
        #unique canidates and number of votes
        if row[2] not in Unique_Candidates:

            Unique_Candidates.append(row[2])
            Vote_Counts.append(1)
        else:

            Candidate_Index = Unique_Candidates.index(row[2])
            Vote_Counts[Candidate_Index] += 1
        

#voting percentage
for i in range(len(Vote_Counts)):
    Vote_Percent.append(Vote_Counts[i] / Total_Votes)

#winner based on votes
for i in range(len(Vote_Counts)):

    if Vote_Counts[i] > Winner_Count:
        Winner_Count = Vote_Counts[i]
        Winner = Unique_Candidates[i]

#analysis output
with open(outputfile, 'w') as text_file:
    text_file.write(f"Election Results\n"
                   f"----------------------------\n"
                   f"Total Votes: {Total_Votes}\n"
                   f"----------------------------\n"
                   )

    for i in range(len(Unique_Candidates)):
        text_file.write(f"{Unique_Candidates[i]}: {fixPercent(Vote_Percent[i])} ({Vote_Counts[i]})\n")

    text_file.write(f"----------------------------\n"
                   f"Winner: {Winner}\n"
                   f"----------------------------\n"
                  )

#textfile and terminal

with open (outputfile, 'r') as analysis_output:
    contents = analysis_output.read()
    print(contents)