# python-challenge
Module 3 challenges for profit/loss calculator and vote tabulator.

# PyBank
## Instructions
In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. You will be given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".

Your task is to create a Python script that analyzes the records to calculate each of the following values:
-The total number of months included in the dataset
-The net total amount of "Profit/Losses" over the entire period
-The changes in "Profit/Losses" over the entire period, and then the average of those changes
-The greatest increase in profits (date and amount) over the entire period
-The greatest decrease in profits (date and amount) over the entire period

## Modules
csv
os
locale

## Summary
This script takes in a csv file of monthly profit or loss data to calculate the total months, total sum of revenue, the average change across the months, as well as highlight the months with the largest increase and decrease in revenues. It outputs the calculations as a text string in both terminal and into a text document. The biggest challenge to this code was working out a way to avoid hard coding the average change calculation, as there is one fewer iteration for average change than there is for the total sum. My solution was a boolean to zero out the first month from the changerecord list we are building in the for loop. This allows the code to work for any similar csv file regardless of the profit/loss. Another challenge was my desire to properly format the output when the result was less than zero. The variables returned would contain the minus-sign on the right of the dollar sign by default. My solution to this was to use a variable to find out if the result was less than zero and then use the locale module and f-strings to concatenate the absolute value of the output in a more visually appealing format. 

## Citations
Researched different ways to format currency, including comma groupings for large numbers. Found locale as a catch-all module for use. https://docs.python.org/3/library/locale.html

After running into errors with directory, found this solution for current working directory https://stackoverflow.com/questions/509742/change-directory-to-the-directory-of-a-python-script

# PyPoll
## Instructions
In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.

You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:
-The total number of votes cast
-A complete list of candidates who received votes
-The percentage of votes each candidate won
-The total number of votes each candidate won
-The winner of the election based on popular vote

## Modules
csv
os

## Summary
This script was designed to read a csv file of a list of ballots to then calculate and return the results of an election. Though the file does contain additional details about each ballot, such as the unique ID and county, we use only the name of the candidates to perform all the actions. Using a for loop, we build a tally of the total votes, build the list of candidates and add to their tally in a dictionary to track the results. It outputs the results of the election, including the overall votes, the votes and percentage for each candidate, as well as declares the winner in both the terminal and an output text file. The biggest challenge in this code was wrapping my head around the order of operations to both build the candidate list and tally their votes in the same for loop. The solution was to logically check if the candidate existed in the list and, if not, add them to it, before processing the tally dictionary. Instead of using the local module, as I did with the banking exercise, I was able to achieve the formatting I wanted through f-string concatencation for the output. 

## Citations
Same as above, after running into errors with directory, found this solution for current working directory. https://stackoverflow.com/questions/509742/change-directory-to-the-directory-of-a-python-script
