#import os
import os
#import csv
import csv

#define variables
count = 0
total = 0
difference = 0
sumDifferences = 0
lastRow = 0
changes = []
dataDict = {}
averageChange = 0
greatestIncrease = 0
greatestIncreaseMonth = ''
greatestDecrease = 0
greatestDecreaseMonth = ''

budget_csv = os.path.join("budget_data.csv")

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Skip the header row first
    csv_header = next(csvfile)

    #Start loop
    for row in csvreader:
        #get total months
        count += 1
        #get total
        total += int(row[1])
        #get difference
        difference = int(row[1]) - lastRow
        #add difference to list
        changes.append(difference)
        #set lastRow for next line to be current value of row[1]
        lastRow = int(row[1])
        #add rows to dict
        dataDict[difference] = row[0]

    #calculate average change
    averageChange = sum(changes)/len(changes)
    #calculate greatest increase in profits
    greatestIncrease = max(changes)
    #calculate greatest decrease
    greatestDecrease = min(changes)

#Print out Financial Analysis
print("Financial Analysis")
print("-------------------------------")
print(f"Total Months: {count}")
print(f"Total: ${total}")
print(f"Average Change: ${averageChange}")
print(f"Greatest Increase in Profits: {dataDict[(greatestIncrease)]} (${greatestIncrease})")
print(f"Greatest Decrease in Profits: {dataDict[(greatestDecrease)]} (${greatestDecrease})")

f = open("Financial_Analysis.txt", "w+")
f.write("Financial Analysis\n")
f.write("-------------------------------\n")
f.write(f"Total Months: {count}\n")
f.write(f"Total: ${total}\n")
f.write(f"Average Change: ${averageChange}\n")
f.write(f"Greatest Increase in Profits: {dataDict[(greatestIncrease)]} (${greatestIncrease})\n")
f.write(f"Greatest Decrease in Profits: {dataDict[(greatestDecrease)]} (${greatestDecrease})\n")

