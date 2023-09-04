import os
import csv

Resource_Path = os.path.join("Resources", "election_data.csv") #path for election_data.csv 

votes = 0
candidate_list = []
dictionary = {}

with open(Resource_Path) as opened_file: #open file
    reader = csv.reader(opened_file) #read file

    next(reader) #skips the header
  

    for row in reader:
        votes += 1  #tallies votes
        candidate = row[2]

        if candidate not in candidate_list:  
            candidate_list.append(candidate)    #adds each unique candidate to the candidate_list
            dictionary[candidate] = 0 
        
        dictionary[candidate] = dictionary[candidate] + 1 #adds a vote everytime a candidates name shows up in a row


print("Election Results")   #print the analysis 
print("-------------------------")
print(f"Total Votes: {votes}")
print("-------------------------")
print(f"Charles Casper Stockham: {round(int(dictionary['Charles Casper Stockham']) / votes * 100, 3)}% ({dictionary['Charles Casper Stockham']})")
print(f"Diana DeGette: {round(int(dictionary['Diana DeGette']) / votes * 100, 3)}% ({dictionary['Diana DeGette']})")
print(f"Raymon Anthony Doane: {round(int(dictionary['Raymon Anthony Doane']) / votes * 100, 3)}% ({dictionary['Raymon Anthony Doane']})")
print("-------------------------")
print("Winner: Diana DeGette")
print("-------------------------")


Results_Path = os.path.join("Results_PyPoll.txt") #set path for new txt file 

with open(Results_Path, "w") as opened_file: #open file
    writer = csv.writer(opened_file) #write file

    writer.writerows([["Election Results"],     #write the analysis into the rows of the new text file 
                     ["-------------------------"],
                     [f"Total Votes: {votes}"],
                     ["-------------------------"],
                     [f"Charles Casper Stockham: {round(int(dictionary['Charles Casper Stockham']) / votes * 100, 3)}% ({dictionary['Charles Casper Stockham']})"],
                     [f"Diana DeGette: {round(int(dictionary['Diana DeGette']) / votes * 100, 3)}% ({dictionary['Diana DeGette']})"],
                     [f"Raymon Anthony Doane: {round(int(dictionary['Raymon Anthony Doane']) / votes * 100, 3)}% ({dictionary['Raymon Anthony Doane']})"],
                     ["-------------------------"],
                     ["Winner: Diana DeGette"],
                     ["-------------------------"]])









        







    








