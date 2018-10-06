import os
import csv
months = 0
profitlosses = 0
prevline = 0
curline = 0 
numofchanges = 0
changebwtmonths = 0


csvpath = os.path.join('budget_data.csv')
with open (csvpath, newline= '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader)
    
    for row in csvreader:
        months = months + 1
        profitlosses = int(row[1]) + profitlosses
        
        
        if (months -1) == 0:
            prevline = int(row[1])
            curline = int(row[1])
            
 #       elif (months -1) == 1:
  #          prevline = curline
  #          curline = int(row[1]) 
   #         changebwtmonths = (curline - prevline)
  #          numofchanges =numofchanges + 1
        else:
            prevline = curline
            curline = int(row[1])
            numofchanges =numofchanges + 1
            changebwtmonths = (((curline) - (prevline)) + changebwtmonths)
                
                 
        
        
        print(row)
        print(prevline)
        print(curline)
        


        
    avgchangeprolos = round(changebwtmonths/numofchanges, 2)
    print(months)
    print(profitlosses)
    print(avgchangeprolos)
