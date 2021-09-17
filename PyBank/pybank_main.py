#import dependencies
import os
import csv

#file location 
budget_data_csv = os.path.join("..", "Resources", "budget_data.csv")

with open (budget_data_csv) as csvfile:
        budget_file = csv.reader( csvfile, delimiter= ",")
        print (budget_file)




