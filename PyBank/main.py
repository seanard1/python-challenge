import os
import csv
import locale

#initialize the locale module for use with currency later
locale.setlocale( locale.LC_ALL, '' )

#declare variables
total = 0
change = 0
changerecord = []
decrease = ["", 0]
increase = ["", 0]
changezero = ""
decreasezero = ""
increasezero = ""
output = []
lastresult = 0
firstpass = True


#Set default directory as same containing active file
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#Create output text file
fileoutput = os.path.join('Analysis', 'analysis.txt')

#Open CSV to start reading, start loop and skip headers
csvpath = os.path.join('Resources', 'budget_data.csv')
with open(csvpath, encoding='UTF-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        header = next(csvreader)
        for row in csvreader:
                
                #For first iteration, set lastresult to zero out with first month profit/loss then set this boolean to false
                if firstpass:
                      lastresult = int(row[1])
                      firstpass = False

                #Increase the total profit/loss sum
                total = total + int(row[1])

                #Find the change for this iteration and save the last result for next iteration; then add that change to the list for later calculations
                change = int(row[1]) - lastresult
                lastresult = int(row[1])
                changerecord.append(change)

                #Check if current iteration change is largest and save
                if change > int(increase[1]):
                        increase[0] = row[0]
                        increase[1] = change
                
                #Check if current iteration change is smallest and save
                if change < int(decrease[1]):
                        decrease[0] = row[0]
                        decrease[1] = change

#These are just for my nitpicking with the output to have the negative sign appear before the $. It checks if the final results will be below zero and remembers for f-string
if sum(changerecord)/(len(changerecord)-1) < 0:
    changezero = "-"
if increase[1] < 0:
    increasezero = "-"
if decrease[1] < 0:
      decreasezero = "-"

#Create the output analysis as a list of strings to print to terminal and output file
output.append('Financial Analysis')
output.append('----------------------------')
output.append('Total months: ' + str(len(changerecord)))
#locale module is nice shortcut to currency formatting with comma grouping for readability
output.append('Total: ' + locale.currency(total, grouping=True))
#remember to subtract one month from the total months, as there is one fewer "change" than months. These f-strings also include my __zero strings to format minus sign before dollar sign
output.append('Average Change: ' + changezero + locale.currency(abs(round(sum(changerecord)/(len(changerecord)-1), 2)), grouping=True))
output.append('Greatest Increase in Profits: ' + increase[0] + ' ' + '(' + increasezero + locale.currency(abs(increase[1]), grouping=True) + ')')
output.append('Greatest Decrease in Profits: ' + decrease[0] + ' ' + '(' + decreasezero + locale.currency(abs(decrease[1]), grouping=True) + ')')

#Print analysis to terminal
for x in range(len(output)):
    print(output[x])

#print analysis to output file
with open(fileoutput, 'w') as file:
       for x in range(len(output)):
              file.write(output[x] + '\n')