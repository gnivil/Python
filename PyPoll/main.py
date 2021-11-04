# Dependacies 
import csv
import os

# Define function to set percentage to 3 decimal points
def fixPercent(num):
    num = "{:.3%}".format(num)
    return num

# Define path for input and output files
inputfile = os.path.join("..", "Python-Challenge", "PyPoll", "Resources", "election_data.csv")
outputfile = os.path.join("..", "Python-Challenge", "PyPoll", "Analysis", "analysis.txt")

# Empty lists to hold calculated values
UniqueCandidates = []
VoteCounts = []
VotePercent = []
TotalVotes = 0
WinnerCount = 0

# Read into CSV and store column values into empty lists
with open(inputfile, 'r') as electiondata:
    reader = csv.reader(electiondata, delimiter=",")
    Headers = next(reader)

    # Calculate the total number of votes cast
    for row in reader: 
        TotalVotes += 1
    
        # Get complete list of candidates who received votes and calculate each one's total number of votes
        # If we reach a unique candidate name, then...
        if row[2] not in UniqueCandidates:

            # Append the name into UniqueCandidates and increase VoteCounts by 1 
            UniqueCandidates.append(row[2])
            VoteCounts.append(1)

        # If the candidate name is already in the list, then...
        else:

            # Reference the Index of the candiate in UniqueCandidates and increase VoteCounts by 1
            CandidateIndex = UniqueCandidates.index(row[2])
            VoteCounts[CandidateIndex] += 1

# Calculate percentage of votes each candidate won
for i in range(len(VoteCounts)):
    VotePercent.append(VoteCounts[i] / TotalVotes)

# Calculate winner of the election based on popular vote
for i in range(len(VoteCounts)):

    # If the number of total votes is greater than WinnerCount, then...
    if VoteCounts[i] > WinnerCount:

        # Update WinnerCount
        WinnerCount = VoteCounts[i]

        # Update Winner
        Winner = UniqueCandidates[i]

# Print output to textfile
with open(outputfile, 'w') as textfile:
    textfile.write(f"Election Results\n"
                   f"----------------------------\n"
                   f"Total Votes: {TotalVotes}\n"
                   f"----------------------------\n"
                   )

    # Iterate through UniqueCandidates to list all candidates and the calculated information
    for i in range(len(UniqueCandidates)):
        textfile.write(f"{UniqueCandidates[i]}: {fixPercent(VotePercent[i])} ({VoteCounts[i]})\n")

    textfile.write(f"----------------------------\n"
                   f"Winner: {Winner}\n"
                   f"----------------------------\n"
                  )

# Print output to terminal
with open (outputfile, 'r') as analysis:
    contents = analysis.read()
    print(contents)