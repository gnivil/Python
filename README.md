# Python-Challenge - Py Me Up, Charlie

-----

# PyBank
Created a Python script for analyzing the financial records of a company. Used financial data called budget_data.csv. The dataset is composed of two columns: Date and Profit/Losses.

## Calculations
* The total number of months included in the dataset
* The net total amount of "Profit/Losses" over the entire period
* Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
* The greatest increase in profits (date and amount) over the entire period
* The greatest decrease in profits (date and amount) over the entire period

```python
 # Dependacies 
import csv
import os
import statistics as st 

# Define function to calculate the average changes of Profit/Losses
def Average(list):
    # Round to the nearest 
    return round(st.mean(list), 2) 

# Define paths for input and output files
inputfile = os.path.join("..", "Python-Challenge", "PyBank", "Resources", "budget_data.csv")
outputfile = os.path.join("..","Python-Challenge", "PyBank", "Analysis", "analysis.txt")

# Empty lists to hold calculated values
Months = []
ProfitLosses = []
ProfitLossesChanges = []

# Read into CSV and store column values into empty lists
with open(inputfile) as budgetdata:
    reader = csv.reader(budgetdata, delimiter=",")
    Headers = next(reader)

    # Append date column to the 'Months' list
    # Append Profits/Losses column to the 'ProfitLosses' list
    for row in reader:
        Months.append(row[0])
        ProfitLosses.append(int(row[1]))

# Calculate net total of Profit/Losses
totalProfLoss = 0
for i in ProfitLosses:
    totalProfLoss = i + totalProfLoss

# Calculate changes in Profit/Losses 
ProfLossChanges = [ProfitLosses[i+1] - ProfitLosses[i] for i in range(0,len(ProfitLosses)-1)]

# Calculate Average change
AverageChange = Average(ProfLossChanges)

# Initialize variables at 0
ProfLossChanges.insert(0,0)
GreatestIncrease = 0
GreatestDecrease = 0

# Caculate greatest increase and decrease in Profit/Losses
for i in range(len(ProfLossChanges)-1):
    if ProfLossChanges[i] < GreatestDecrease:
        GreatestDecrease = ProfLossChanges[i]

    if ProfLossChanges[i] > GreatestIncrease:
        GreatestIncrease = ProfLossChanges[i]   


# Find index for Greatest Increase and Greatest Decrease
GIindex = ProfLossChanges.index(GreatestIncrease)
GDindex = ProfLossChanges.index(GreatestDecrease)

# Use index to determine date
GIdate = Months[GIindex]
GDdate = Months[GDindex]
    
# Create output
analysis= (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total months: {len(Months)}\n"
    f"Total: ${totalProfLoss}\n"
    f"Average Change: ${AverageChange}\n"
    f"Greatest Increase in Profits: {GIdate} (${GreatestIncrease})\n"
    f"Greatest Decrease in Profits: {GDdate} (${GreatestDecrease})\n"
)

# Print analysis to terminal
print(analysis)

# Print analysis to textfile
with open(outputfile, 'w') as textfile:
    textfile.write(analysis)
```
## Analysis Output

![alt text](https://github.com/gnivil/Python-Challenge/blob/b6156db27ed7c5f7bfe181396ef999f39b96b09e/PyBank/Analysis/PyBank%20Analysis.png)

-----

# PyPoll
Helped a small, rural town modernize its vote counting process by creating a Python script that analyzes the votes. Used a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate.

## Calculations
* The total number of votes cast
* A complete list of candidates who received votes
* The percentage of votes each candidate won
* The total number of votes each candidate won
* The winner of the election based on popular vote.

```python
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
```

## Analysis Output

![alt text](https://github.com/gnivil/Python-Challenge/blob/c129d552965b1ad39ac4f3c90f406f3733725f9c/PyPoll/Analysis/PyPoll%20Analysis.png)