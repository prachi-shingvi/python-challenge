import csv

# declaring variables
totalvotes=0
votes={}
maxvotes=0
winner=""

# path to csv file
path="./Resources/election_data.csv"

# reading csv file
with open(path,'r') as file:
    csvfile=csv.reader(file,delimiter=",")

    # storing header row
    header=next(csvfile)

    # looping through each row in dataset
    for row in csvfile:
        # calculating total number of votes
        totalvotes=totalvotes+1
        candidate=row[2]

        # populating dictionary of candidates and corresponding votes
        if candidate in votes:
            votes[candidate]+=1
        else:
            votes[candidate]=1

    # Displaying on Terminal
    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str(totalvotes))
    print("-------------------------")

    for candidate in votes:
        votecount=votes[candidate]

        # calculating percent vote
        votepercent=round((votecount/totalvotes) * 100,3)

        # finding winner candidate
        if votecount > maxvotes:
            maxvotes=votecount
            winner=candidate


        print(candidate + ": " + str(votepercent) + "% (" + str(votecount) + ")")

    print("-------------------------")
    print("Winner: " +  winner)
    print("-------------------------")

# declaring output file path
output="./Analysis/Output.txt"

# exporting results to .txt file 
with open(output,'w') as stream:
    stream.write("Election Results\n")
    stream.write("-------------------------\n")
    stream.write("Total Votes: " + str(totalvotes) + "\n")
    stream.write("-------------------------\n")
    for candidate in votes:
        votecount=votes[candidate]
        votepercent=round((votecount/totalvotes) * 100,3)

        if votecount > maxvotes:
            maxvotes=votecount
            winner=candidate


        stream.write(candidate + ": " + str(votepercent) + "% (" + str(votecount) + ")\n")
    stream.write("-------------------------\n")
    stream.write("Winner: " +  winner + "\n")
    stream.write("-------------------------\n")


    