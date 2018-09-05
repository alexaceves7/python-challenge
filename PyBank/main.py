#main.py for PyBank

#add imports
import os
import csv
months = 0
total_profit = 0
month_change = 0
previous_month = 0
change = []
d = {}

#read csv file
csvpath = os.path.join('.','Resources','budget_data.csv')

#split up rows and add delimiter
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next (csvreader) #moves to next row to avoide header
    count = 0
    for row in csvreader: #going to go through each row
        months = months + 1 #keeps count of total months
        total_profit = total_profit + int(row[1]) #adds up total
        month_change = float(row[1]) - previous_month #finds the monthly change
        if previous_month != 0: #to avoid including the first row of data since no previous month data
            change.append(month_change) #appends to change 
            d[str(row[0])] = round(month_change, 1)#adds change and the month to a dictionary
        previous_month = float(row[1]) #makes the current month the previous month before going to next row
        
    
    
    
    #calculates average change and saves it to varisble
    average_change = round((sum(change)/len(change)), 2)
   
    
    #gets the max and min from the d dictionary
    maximum = max(d, key=d.get) 
          
    minimum = min(d, key=d.get)

# prints everything to pybank txt file
with open("pybank.txt", "w") as text_file:
    print ('Financial Analysis', file=text_file)
    print ('----------------------------', file=text_file)
    print (f'Total Months: {months}',file=text_file)
    print (f'Total : ${total_profit}',file=text_file)
    print (f'Average Change: ${average_change}',file=text_file)
    print (f'Greatest Increase in Profits: {maximum} (${int(d[maximum])})',file=text_file)
    print (f'Greatest Decrease in Profits: {minimum} (${int(d[minimum])})',file=text_file)

#prints evrything to terminal
print ('Financial Analysis')
print ('----------------------------')
print (f'Total Months: {months}')
print (f'Total : ${total_profit}')
print (f'Average Change: ${average_change}')
print (f'Greatest Increase in Profits: {maximum} (${int(d[maximum])})')
print (f'Greatest Decrease in Profits: {minimum} (${int(d[minimum])})')