#import packages
import csv
import os
import statistics as stat #to calculate average

#function to calculate average of the list
def Average(list):

    #format number to 2 decimals
    return round(stat.mean(list), 2) 

#path for the input and output files
inputfile = os.path.join("Resources", "budget_data.csv")
outputfile = os.path.join("analysis", "pybank_analysis.txt")

#create empty lists
Dates = []
Prof_Loss = []
Prof_Loss_Changes = []

#read the CSV file and store values of each column into lists
with open(inputfile, 'r') as budgetdata:
    budget_reader = csv.reader(budgetdata, delimiter=",")
    Headers = next(budget_reader)

    for row in budget_reader:
        Dates.append(row[0])
        Prof_Loss.append(int(row[1]))

#Profits/Losses list and calculate total
Total_Prof_Loss = 0
for i in Prof_Loss:
    Total_Prof_Loss = i + Total_Prof_Loss

Prof_Loss_Changes = [Prof_Loss[i+1] - Prof_Loss[i] for i in range(0,len(Prof_Loss)-1)]

#calculate average change by calling the function and store in variable ---
Avg_Change = Average(Prof_Loss_Changes)

#reseting variables
Prof_Loss_Changes.insert(0,0)
Grst_Increase = 0
Grst_Decrease = 0

#calculate greatest decrease and greatest increase
for i in range(len(Prof_Loss_Changes)-1):
    if Prof_Loss_Changes[i] < Grst_Decrease:
        Grst_Decrease = Prof_Loss_Changes[i]

    if Prof_Loss_Changes[i] > Grst_Increase:
        Grst_Increase = Prof_Loss_Changes[i]   


GIindex = Prof_Loss_Changes.index(Grst_Increase)
GDindex = Prof_Loss_Changes.index(Grst_Decrease)

GIdate = Dates[GIindex]
GDdate = Dates[GDindex]
    
#analysis output
analysis_output = (f"Financial Analysis\n"
                  f"----------------------------\n"
                  f"Total Months: {len(Dates)}\n"
                  f"Total: ${Total_Prof_Loss}\n"
                  f"Average Change: ${Avg_Change }\n"
                  f"Greatest Increase in Profits: {GIdate} (${Grst_Increase})\n"
                  f"Greatest Decrease in Profits: {GDdate} (${Grst_Decrease})\n"
)

#terminal
print(analysis_output)

#text file
with open(outputfile, 'w') as textfile:
    textfile.write(analysis_output)

