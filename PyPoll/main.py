import os
import csv

filepath = os.path.join('Resources','election_data.csv')
outputFile=os.path.join('analysis','Election_results.txt')

cand_dict={}
with open(filepath) as eleDataFile:
    eleDataReader = csv.reader(eleDataFile,delimiter=',')

    eleData_header = next(eleDataReader)
    totalVotes = len(list(eleDataReader))
    print(totalVotes)
    for row in range(5):#eleDataReader:
        #do stuff here
        something = row

# set up text results:
txtheader="Election Results"
txtdivider="-------------------------------"
txtTotVotes=f"Total Votes: {totalVotes}"
#df was ordered in value_counts, so 1st candidate is the one with the most votes
txtWinner = f'Winner: ' #fixthis{candList_df["Candidate"][0]}'

with open(outputFile, "a") as output:
    print(txtheader, file=output)
    print(txtheader)
    print(txtdivider, file=output)
    print(txtdivider)
    print(txtTotVotes, file=output)
    print(txtTotVotes)
#    for row in candList_df.iterrows():
        #fixthistxtCand =f'{row[1]["Candidate"]}: {round(row[1]["Pct"],2)}% ({row[1]["NumVotes"]})'
#        print(txtCand)
#        print(txtCand, file=output)

    print(txtdivider, file=output)
    print(txtdivider)
    print(txtWinner, file=output)
    print(txtWinner)
    print(txtdivider, file=output)
    print(txtdivider)


# would argue this is easier using pandas.
# could simply build a df, use value_counts to count the votes, order it (below code) and put results in new df.
# Then can iterate through the candList_df to show the results, the 1st cand would be the winner when ordered descending (ascending=False)
#import pandas as pd
#eldata_df = pd.read_csv(filepath, encoding ='UTF-8')

#totalVotes=eldata_df["Voter ID"].count()
# get the counts for each candidate, make it a df, reset index and rename columns
#candList_df=eldata_df["Candidate"].value_counts(ascending=False).to_frame().reset_index().rename(columns = {"index":"Candidate","Candidate":"NumVotes"})
#pctVote=(candList_df["NumVotes"]/totalVotes)*100
#candList_df["Pct"]=pctVote