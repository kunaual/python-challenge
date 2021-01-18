import os
import csv 

csvPath=os.path.join('Resources','budget_data.csv')
outputFile=os.path.join('analysis','analysis.txt')

#initalize variables
totalMth = 0
netPLtot = 0
greatestIncMth = 'Jan-2010'
greatestInc = 0
greatestDecrMth ='Jan-2010'
greatestDecr = 0
prevRowMth = 'never'
prevRowPL=0
avgChg=0
with open(csvPath) as budDataFile:
    budDataReader = csv.reader(budDataFile,delimiter=',')

    budData_header = next(budDataReader)
#  len(list(budDataReader)  use this for totalmths
    for row in budDataReader:

        currMth=row[0]
        currPL=int(row[1])
        if prevRowMth!='never': #not on the first row of data
            #calculate change between prev mth and this one
            currChg = currPL - prevRowPL 
            avgChg+=currChg
            if currChg>0 and currChg>greatestInc:
                greatestInc=currChg
                greatestIncMth=currMth
            elif currChg<0 and currChg<greatestDecr:
                greatestDecr = currChg
                greatestDecrMth = currMth



        totalMth+=1
        netPLtot+=currPL

        prevRowMth=currMth
        prevRowPL=currPL

# set up text results:
txtheader="Financial Analysis"
txtdivider="-------------------------------"
txtTotM=f"Total Months: {totalMth}"
txtTotPL=f"Total: ${netPLtot}"
txtAvgC=f"Average Change:${round(avgChg/(totalMth-1),2)}"
txtGrIn=f"Greatest Increase in Profits: {greatestIncMth} (${greatestInc})"
txtGrDe=f"Greatest Decrease in Profits: {greatestDecrMth} (${greatestDecr})"

with open(outputFile, "a") as output:
    print(txtheader, file=output)
    print(txtdivider, file=output)
    print(txtTotM, file=output)
    print(txtTotPL, file=output)
    print(txtAvgC, file=output)
    print(txtGrIn, file=output)
    print(txtGrDe, file=output)

print(txtheader)
print(txtdivider)
print(txtTotM)
print(txtTotPL)
print(txtAvgC)
print(txtGrIn) 
print(txtGrDe)
