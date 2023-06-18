import csv

# declaring variables
totalmonths=0
totalAmt=0
profitLossArr = []
totalDifference = 0
AvgChange=0.00
greatestIncrease=float("-inf")
greatestIncreaseMonth=""
greatestDecreaseMonth=""
greatestDecrease=float("inf")

# path to csv file
path = './Resources/budget_data.csv'

# reading csv file
with open (path,'r') as file:

    csvfile=csv.reader(file,delimiter=",")

    # storing header row
    header=next(csvfile)

    # looping through each row in dataset
    for row in csvfile:

        totalAmt=totalAmt+int(row[1])
        totalmonths+=1

        #creating array for easier calculation of profit/loss increase/decrease over each months
        profitLossArr.append(row)
    
    # calculating greatestIncrease and greatestDecrease by looping over profitlossArr
    for i in range(len(profitLossArr)):
        amt = profitLossArr[i][1]
        if i != 0:
            currentDiff=int(profitLossArr[i][1]) - int(profitLossArr[i-1][1])
            
            if(greatestIncrease<currentDiff):
                greatestIncrease=currentDiff
                greatestIncreaseMonth=profitLossArr[i][0]

            if(greatestDecrease>currentDiff):
                greatestDecrease=currentDiff
                greatestDecreaseMonth=profitLossArr[i][0]
            
            totalDifference = totalDifference + currentDiff
            
    
    AvgChange=round(totalDifference/(totalmonths-1),2)

    
# Displaying on Terminal
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(totalmonths))
print("Total: $" + str(totalAmt))
print("Average Change: $"+ str(AvgChange))
print("Greatest Increase in Profits: " + greatestIncreaseMonth+" ($" + str(greatestIncrease) + ")")
print("Greatest Decrease in Profits: " + greatestDecreaseMonth+" ($" + str(greatestDecrease) + ")")

# declaring output file path
output="./Analysis/Output.txt"

# exporting results to .txt file 

with open(output,'w') as stream:
    stream.write("Financial Analysis\n")
    stream.write("----------------------------\n")
    stream.write("Total Months: " + str(totalmonths) + "\n")
    stream.write("Total: $" + str(totalAmt) + "\n")
    stream.write("Average Change: $"+ str(AvgChange) + "\n")
    stream.write("Greatest Increase in Profits: " + greatestIncreaseMonth+" ($" + str(greatestIncrease) + ")" + "\n")
    stream.write("Greatest Decrease in Profits: " + greatestDecreaseMonth+" ($" + str(greatestDecrease) + ")" + "\n")
    




