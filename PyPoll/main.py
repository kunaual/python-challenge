import os
import csv

filepath = os.path.join('Resources','election_data.csv')
outputFile=os.path.join('analysis','Election_results.txt')

cand_dict={}
with open(filepath) as eleDataFile:
    eleDataReader = csv.reader(eleDataFile,delimiter=',')

    eleData_header = next(eleDataReader)

    totalVotes = 0
    for row in eleDataReader:
        cand=row[2]
        if cand in cand_dict:
            cand_dict[cand]=cand_dict[cand]+1 
        else:
            cand_dict[cand]=1
        totalVotes+=1
        #if totalVotes>5:  # for testing
        #    break

# set up text for results:
txtheader="Election Results"
txtdivider="-------------------------------"
txtTotVotes=f"Total Votes: {totalVotes}"

winner = "nobody"

with open(outputFile, "a") as output:
    print(txtheader, file=output)
    print(txtheader)
    print(txtdivider, file=output)
    print(txtdivider)
    print(txtTotVotes, file=output)
    print(txtTotVotes)
    print(txtdivider, file=output)
    print(txtdivider)
    for cand, votes in cand_dict.items():
        if winner=='nobody':
            #on first cand, just set winner = this person
            winner = cand
        else:
            #check if current cand has more votes than winner + update winner
            if votes > cand_dict[winner]:
                winner = cand
        pct = (votes/totalVotes)*100
        #:.3f to display just 3 decimal places for the %
        txtCand =f'{cand}: {pct:.3f}% ({votes})'
        print(txtCand)
        print(txtCand, file=output)

    print(txtdivider, file=output)
    print(txtdivider)
    txtWinner = f'Winner: {winner}'
    print(txtWinner, file=output)
    print(txtWinner)
    print(txtdivider, file=output)
    print(txtdivider)

# another solution using pandas:
# could simply read file to df, use value_counts to count the votes, order it and put results in new df. (below code)
# Then can iterate through the candList_df to show the results, the 1st cand would be the winner when ordered descending (ascending=False)
#import pandas as pd
#eldata_df = pd.read_csv(filepath, encoding ='UTF-8')

#totalVotes=eldata_df["Voter ID"].count()
# get the counts for each candidate, make it a df, reset index and rename columns
#candList_df=eldata_df["Candidate"].value_counts(ascending=False).to_frame().reset_index().rename(columns = {"index":"Candidate","Candidate":"NumVotes"})
#pctVote=(candList_df["NumVotes"]/totalVotes)*100
#candList_df["Pct"]=pctVote