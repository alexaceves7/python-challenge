#main.py for PyPoll

#add imports
import os
import csv
#set up all variables I will need
total_votes = 0 #keep count of votes
khan = 0 #keep count of khan votes
correy = 0 #keep count of correy votes
li = 0 #keep count of li votes
otooly = 0 #keep count pf otooly votes
candidates = [] #list for candidates
d = {} #dictionary for results to gert max

#read csv file
csvpath = os.path.join('.','Resources','election_data.csv')

with open(csvpath, newline='') as csvfile: #will go through each row
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    for row in csvreader:
        total_votes = total_votes + 1 #adds to vote total
        if row[2] not in candidates: #adds to candidate list
            candidates.append(row[2])
            
        
        if row[2] == "Khan": #counts only khan votes
            khan = khan + 1
        elif row[2] == "Correy": #counts only correy votes
            correy = correy + 1
        elif row[2] == "Li": #counts only li votes
            li = li + 1
        else:
            otooly = otooly + 1 #counts only ottoley votes
        
        
        #finds percent of total for each candidate and stores it
        percent_khan = '{percent:.2%}'.format(percent=khan/total_votes)
        percent_correy = '{percent:.2%}'.format(percent=correy/total_votes)    
        percent_li = '{percent:.2%}'.format(percent=li/total_votes)
        percent_otooly = '{percent:.2%}'.format(percent=otooly/total_votes)
        
        
        #adds to dictionary the candidate, percent and total votes
        d["Khan"] = [percent_khan, khan]
        d["Correy"] = [percent_correy, correy]
        d["Li"] = [percent_li, li]
        d["O'Tooley"] = [percent_otooly, otooly]
    
#finds max from the dictionary
maximum = max(d, key=d.get)

#prints to pypoll txt file
with open("pypoll.txt", "w") as text_file:
    print ('Election Results', file=text_file)
    print ('---------------------------', file=text_file)
    print (f'Total Votes: {total_votes}', file=text_file)
    print ('---------------------------', file=text_file)
    print (f'Khan: {percent_khan} ({khan})', file=text_file)
    print (f'Correy: {percent_correy} ({correy})', file=text_file)
    print (f'Li: {percent_li} ({li})', file=text_file)
    print (f"O'Tooley: {percent_otooly} ({otooly})", file=text_file)
    print ('---------------------------', file=text_file)
    print (f'Winner: {maximum}', file=text_file)
    print ('---------------------------', file=text_file)

#prints to terminal
print ('Election Results')
print ('---------------------------')
print (f'Total Votes: {total_votes}')
print ('---------------------------')
print (f'Khan: {percent_khan} ({khan})')
print (f'Correy: {percent_correy} ({correy})')
print (f'Li: {percent_li} ({li})')
print (f"O'Tooley: {percent_otooly} ({otooly})")
print ('---------------------------')
print (f'Winner: {maximum}')
print ('---------------------------')