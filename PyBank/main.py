 # Dependacies 
import csv
import os
import statistics as st 

# Define function to calculate the average changes of Profit/Losses
def Average(list):
    # Round to the nearest 
    return round(st.mean(list), 2) 

# Define paths for input and output files
inputfile = os.path.join('..', 'Resources', 'budgetdata.csv')
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