# Module 3 _Challenge3:PyBank
# Objective 1: Import modules s and csv
import os
import csv
# Objetcive 2: Set the path for the csv file in PyBAnk folder
PyBankcsv= os.path.join("Resources" , "budget_data.csv")

# Objective 3: Creating the lists
profit=[]
monthlyChanges=[]
monthlyChangesProfits=[]
date=[]

# The variables
count=0
totalprofit=0
initialprofit=0


# Open the csv using path PyBankcsv
with open (PyBankcsv, newline="") as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")
    csvheader= next(csvreader)
    firstRow=next(csvreader)
    count +=1
    totalprofit += int(firstRow[1])
    prevNet= int(firstRow[1])

# using loop calculating the months with in csv reader

    for row in  csvreader:
    # Count the number in the dataset
        count += 1
        # Calculating the total and change profits
        totalprofit += int(row[1])
        monthlyChanges= int(row[1])
        prevnet= int (row[1])
        monthlyChangesProfits += [monthlyChanges]
        date += (row[0])

 # Calculating the average change in profits
totalChangeProfits= sum(monthlyChangesProfits)/len(monthlyChangesProfits)

# The greatest increase and decrease in profits
greatestIncreaseProfits= max(monthlyChangesProfits)
greatestdecreaseProfits= min(monthlyChangesProfits)

increaseDate= date[monthlyChangesProfits.index(greatestIncreaseProfits)]
decreaseDate=date[monthlyChangesProfits.index(greatestdecreaseProfits)]

print(greatestIncreaseProfits)
print("----------------------------")

# Print to a text file: financialAnalysis.txt
with open('financialAnalysis.txt','w') as text:

    text.write("--------------------------------\n")
    text.write("financial Analysis"+ "\n")
    text.write("----------------\n\n")
    text.write("Total Months:"+ str(count)+"\n")
    text.write("Total Profits:"+ "$"+ str(totalprofit)+ "\n")
    text.write(f" Average Change: $ {totalChangeProfits:2f}\n")
    text.write("Greatest Increase in Profits:"+str(increaseDate)+"($"+str(greatestIncreaseProfits)+")\n")
    text.write("Greatest Decrease in Profits:"+str(decreaseDate)+"($"+str(greatestdecreaseProfits)+")\n")
    text.write("\n")

    text.write("----------------------\n")




