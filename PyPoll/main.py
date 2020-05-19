#import os
import os
#import csv
import csv

#Define variables
count = 0
candidate = ''
percentWon = 0.0
totalVotes = 0
khanVotes = 0
correyVotes = 0
liVotes = 0
otooleyVotes = 0
khanPercent = 0.0
correyPercent = 0.0
liPercent = 0.0
otooleyPercent = 0.0
#voterDict = {Candidate, percentWon, totalVotes(per candidate)}
voterDict = {}
resultsList = []


poll_csv = os.path.join("election_data.csv")

with open(poll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Skip the header row first
    csv_header = next(csvfile)

    #Start loop
    for row in csvreader:
        #get total number of votes
        count += 1
        #get total number of votes per
        if row[2] == "Khan":
            khanVotes += 1
        elif row[2] == "Correy":
            correyVotes += 1
        elif row[2] == "Li":
            liVotes += 1
        elif row[2] == "O'Tooley":
            otooleyVotes += 1
    #Calculate percentage results
    khanPercent = khanVotes/count
    correyPercent = correyVotes/count
    liPercent = liVotes/count
    otooleyPercent = otooleyVotes/count

    #add winning percentages to dict
    voterDict[khanPercent] = "Khan"
    voterDict[correyPercent] = "Correy"
    voterDict[liPercent] = "Li"
    voterDict[otooleyPercent] = "O'Tooley"

    resultsList = [khanPercent, correyPercent, liPercent, otooleyPercent]

    #Decide winner
    winner = max(resultsList)

    #Format percentage into .000%
    khanPercent = "{:.3%}".format(khanPercent)
    correyPercent = "{:.3%}".format(correyPercent)
    liPercent = "{:.3%}".format(liPercent)
    otooleyPercent = "{:.3%}".format(otooleyPercent)

#Print out Voter Analysis
print("Election Results")
print("-----------------------")
print(f"Total Votes: {count}")
print("-----------------------")
print(f"Khan: {khanPercent} ({khanVotes})")
print(f"Correy: {correyPercent} ({correyVotes})")
print(f"Li: {liPercent} ({liVotes})")
print(f"O'Tooley: {otooleyPercent} ({otooleyVotes})")
print("-----------------------")
print(f"Winner: {voterDict[(winner)]}")
print("-----------------------")

f = open("Election_Results.txt", "w+")
f.write("Election Results\n")
f.write("-----------------------\n")
f.write(f"Total Votes: {count}\n")
f.write("-----------------------\n")
f.write(f"Khan: {khanPercent} ({khanVotes})\n")
f.write(f"Correy: {correyPercent} ({correyVotes})\n")
f.write(f"Li: {liPercent} ({liVotes})\n")
f.write(f"O'Tooley: {otooleyPercent} ({otooleyVotes})\n")
f.write("-----------------------\n")
f.write(f"Winner: {voterDict[(winner)]}\n")
f.write("-----------------------\n")