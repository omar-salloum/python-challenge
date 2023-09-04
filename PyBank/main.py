import os
import csv


CSV_PATH = os.path.join("Resources", "budget_data.csv")


net = 0 
months = 0



with open(CSV_PATH) as opened_file: #open file
    reader = csv.reader(opened_file) #read file
    next(reader) #skip header 
    

    for row in reader:
        months += 1                     #count number of months 
        current_month = row[0]          #set each row[0] to variable current_month
        current_profit = int(row[1])    #set each row[1] to variable current_profit
        net += current_profit           #calculate net profit/loss 

#file is closed.

with open(CSV_PATH) as opened_file: #open file
    reader = csv.reader(opened_file) #read file
    
    next(reader) #skip header

    previous = int(next(reader)[1]) #store first value and skip to the next row 

    total = 0
    max = 0
    min = 0
    
    for row in reader:

        change = int(row[1]) - previous #the change in profit loss for every period
        total = total + change #the sum of the changes in profit/loss 
        previous = int(row[1]) #reassign the previous value to the current row 

        if change > max: #checks whether each change is higher than the current highest change 
            max = change #stores highest change 
            max_date = row[0] #stores date for highest change 

        if change < min: #checks whether each change is a smaller number than the current smallest numbered change 
            min = change #stores change value with the lowest number  
            min_date = row[0] #stores date for change value with the lowest numbest 
        
AvgChange = round((total / (int(months) - 1)), 2) #Calculates the average change for the sum of the periods changes 


print("Financial Analysis") #print all the info to the terminal ...
print("----------------------------")
print(f"Total Months: {months}")
print(f"Total: ${net}")
print(f"Average Change: ${AvgChange}")
print(f"Greatest Increase in Profits: {max_date} (${max})")
print(f"Greatest Decrease in Profits: {min_date} (${min})")


Results_Path = os.path.join("Results.txt") #set path for new txt file 

with open(Results_Path, "w") as opened_file: #open file
    writer = csv.writer(opened_file) #write file


    writer.writerows([["Financial Analysis"], #write the info in the text file 
                      ["----------------------------"], 
                      [f"Total Months: {months}"], 
                      [f"Total: ${net}"], 
                      [f"Average Change: ${AvgChange}"], 
                      [f"Greatest Increase in Profits: {max_date} (${max})"], 
                      [f"Greatest Decrease in Profits: {min_date} (${min})"]])

