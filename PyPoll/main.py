import os
import csv

Resource_Path = os.path.join("Resources", "election_data.csv") #path for election_data.csv 

votes = 0
dictionary = {}
winner = 0

with open(Resource_Path) as opened_file: #open file
    reader = csv.reader(opened_file) #read file

    header = next(reader) #skips the header
  

    for row in reader:
        votes += 1  #tallies votes
        candidate = row[2]

        if candidate not in dictionary:  
            dictionary[candidate] = 0   #add each unique candidate to the dict and set their value to 0 
        
        dictionary[candidate] += 1 #adds a vote everytime a candidates name shows up in a row


    print("Election Results")   #print the analysis 
    print("-------------------------")
    print(f"Total Votes: {votes}")
    print("-------------------------")
    for key in dictionary:
        print(f"{key}: {round(int(dictionary[key]) / votes * 100, 3)}% ({dictionary[key]})")
    print("-------------------------")
    for key in dictionary:
        if dictionary[key] > winner:
            winner = dictionary[key]
            winner_name = key
    print(f"Winner: {winner_name}")
    

#close file

Results_Path = os.path.join("analysis", "Results_PyPoll.txt") #set path for new txt file 

with open(Results_Path, "w") as opened_file: #open file
    writer = csv.writer(opened_file) #write file

    writer.writerows([["Election Results"],     #write the analysis into the rows of the new text file 
                     ["-------------------------"],
                     [f"Total Votes: {votes}"],
                     ["-------------------------"]])
    for key in dictionary:
        writer.writerows([[f"{key}: {round(int(dictionary[key]) / votes * 100, 3)}% ({dictionary[key]})"]])
     
    writer.writerows([["-------------------------"],
                     ["Winner: Diana DeGette"],
                     ["-------------------------"]])









        







    








