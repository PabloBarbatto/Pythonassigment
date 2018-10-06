import os
import csv
months = 0
profitlosses = 0
prevline = 0
curline = 0 
numofchanges = 0
changebwtmonths = 0
maxchg = 0
minchg = 0 
maxdate = str
mindate = str

csvpath = os.path.join('budget_data.csv')
with open (csvpath, newline= '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader)
    
    for row in csvreader:
        months = months + 1
        profitlosses = int(row[1]) + profitlosses
        #prevline = curline
        #curline = int(row[1])
        
        if (months -1) == 0:
            prevline = int(row[1])
            curline = int(row[1])     
        else:
            prevline = curline
            curline = int(row[1])
            numofchanges =numofchanges + 1
            changebwtmonths = (((curline) - (prevline)) + changebwtmonths)
            if maxchg < (curline - prevline):
                maxchg = (curline - prevline)
                maxdate = str(row[0])
            else:
                maxchg = maxchg
            if minchg > (curline - prevline):
                minchg = (curline - prevline)
                mindate = str(row[0])
            else:
                minchg = minchg     
        
        

avgchangeprolos = round(changebwtmonths/numofchanges, 2)

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(months))
print("Total: $"+str(profitlosses))
print("Average  Change: $"+str(avgchangeprolos))
print("Greatest Increase in Profits: " + maxdate + " (" +str(maxchg) + ")")
print("Greatest Decrease in Profits: " + mindate + " (" +str(minchg) + ")")

output_dest = os.path.join('pybank_output.txt')
with open(output_dest, 'w') as writefile:
    writefile.write("Financial Analysis\n")
    writefile.write("----------------------------\n")
    writefile.write("Total Months: " + str(months)+"\n")
    writefile.write("Total: $"+str(profitlosses) +"\n")
    writefile.write("Average  Change: $"+str(avgchangeprolos)+"\n")
    writefile.write("Greatest Increase in Profits: " + maxdate + " (" +str(maxchg) + ")"+"\n")
    writefile.write("Greatest Decrease in Profits: " + mindate + " (" +str(minchg) + ")"+"\n")