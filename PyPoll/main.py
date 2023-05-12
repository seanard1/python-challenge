import os
import csv

#Set default directory as same containing active file
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#Declare variables
votes = 0
tally = {}
candidates = []
results = []
winningtotal = 0
winner = ""

#Create output text file
fileoutput = os.path.join('Analysis', 'results.txt')

#Open CSV to start reading as a dictionary, start loop and skip headers
csvpath = os.path.join('Resources', 'election_data.csv')
with open(csvpath, encoding='UTF-8') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=",")
        for row in csvreader:
                
                #Add to total vote tally
                votes = votes + 1

                #Set current ballot choice by name
                currentballot = row["Candidate"]

                #Add candidate if it's their first vote
                if currentballot not in candidates:
                     candidates.append(currentballot)
                     tally[currentballot] = 0

                #Update total vote dictionary for current ballot
                tally[currentballot] = tally[currentballot] + 1
                
#Build results list of strings for eventual output
results.append('Election Results')
results.append('-------------------------')
results.append('Total Votes: ' + f"{votes:,}")
results.append('-------------------------')

#Loop to print results for each candidate to results
for x in range(len(candidates)):
       results.append(candidates[x] + ": " + f"{round(tally[candidates[x]]/votes*100, 2):,}" + "% (" + f"{tally[candidates[x]]:,}" + ")")
results.append('-------------------------')

#Loop to find winner and add to results
for x in range(len(candidates)):
       if tally[candidates[x]] > winningtotal:
            winner =  candidates[x]
            winningtotal = tally[candidates[x]]
results.append('Winner: ' + winner)
results.append('-------------------------')

#print results to terminal
for x in range(len(results)):
    print(results[x])

#print analysis to output file
with open(fileoutput, 'w') as file:
       for x in range(len(results)):
              file.write(results[x] + '\n')