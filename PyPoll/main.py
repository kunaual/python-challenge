import os
import pandas as pd

filepath = os.path.join('Resources','election_data.csv')

eldata_df = pd.read_csv(filepath, encoding ='UTF-8')
print(eldata_df.shape)
totalVotes=eldata_df["Voter ID"].count()
# get the counts for each candidate, make it a df, reset index and rename columns
candList_df=eldata_df["Candidate"].value_counts(ascending=False).to_frame().reset_index().rename(columns = {"index":"Candidate","Candidate":"NumVotes"})
#candList_df=candList.rename(columns = {"index":"Candidate","Candidate":"NumVotes"})

pctVote=(candList_df["NumVotes"]/totalVotes)*100

candList_df["Pct"]=pctVote
print(candList_df)#.loc[0]["Candidate"])
#  * The total number of votes cast
#  * A complete list of candidates who received votes
#  * The percentage of votes each candidate won
#  * The total number of votes each candidate won
# * The winner of the election based on popular vote.

# set up text results:
txtheader="Election Results"
txtdivider="-------------------------------"
print(txtheader)
print(txtdivider)
#for candName, numVotes, pctVote in candList_df.iteritems():
#    print(f"{candName}: {round(pctVote,3)}% ({numVotes})")
for row in candList_df.iterrows():
    print(f'{row[1]["Candidate"]}: {round(row[1]["Pct"],2)}% ({row[1]["NumVotes"]})')

print(txtdivider)
