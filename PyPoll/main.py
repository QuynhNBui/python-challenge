import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

#initialize variables
vote_count = 0
#candidate dictionary:
candidate_vote = {}

# read csv file
with open(csvpath,newline ="") as election_file:
    election_data = csv.reader(election_file, delimiter = ",")
    
    #read the header first
    header = next(election_data)
    
    #get total count and list of candidates and thei count
    for row in election_data:
        vote_count += 1
        candidate_vote[row[2]] = candidate_vote.get(row[2],0) + 1
    
    #find the winner:
    most_vote = max(candidate_vote.values())
    winner = [k for k, v in candidate_vote.items() if v == most_vote]

output_path = os.path.join("PyPoll_Report.txt" )

#write txt file
with open(output_path,"w") as output_file:
    output_file.writelines("\n___________________________\n")
    output_file.writelines("Election Results\n")
    output_file.writelines("\n___________________________\n")
    output_file.writelines(f"Total Votes: {vote_count} \n")
    output_file.writelines("___________________________\n")  
    for k, v in candidate_vote.items():
        output_file.writelines(k + ":" + "{:.3%}".format(v/vote_count)+" (" + str(v)+")"+"\n")
    
    output_file.writelines("\n___________________________\n")
    output_file.writelines(f"Winner: {winner[0]} \n")
    output_file.writelines("___________________________\n")

#read output file       
with open(output_path,"r") as result_file:
    print(result_file.read())  