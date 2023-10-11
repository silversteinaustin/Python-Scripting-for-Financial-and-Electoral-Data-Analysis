import pandas as pd

#Create a file path across directory
import os

#Import the CSV file
import csv

csvpath = os.path.join('Resources','election_data.csv')

#Read the CSV file into a Pandas DataFrame
df = pd.read_csv(csvpath)

#Calculate the total number of votes cast
total_votes_cast = df.shape[0]

#Print results
print('Total Votes: ', total_votes_cast)

#Create a new DF to store the results
results_df = pd.DataFrame (columns=['Candidate', 'Percent of Votes Won', 'Total Number of Votes Won'])

#Loop through the data frame and calculate the % of votes and total votes won for each candidate
for candidate in df['Candidate'].unique():
    number_of_votes = df[df['Candidate'] == candidate].shape[0]
    percent_of_votes = number_of_votes/total_votes_cast*100

    results_df = results_df.append({'Candidate': candidate, 'Percent of Votes Won':percent_of_votes, 'Total Number of Votes Won': number_of_votes},ignore_index=True)

#Convert the Total Number of Votes Won column to an integer column
results_df['Total Number of Votes Won'] = results_df['Total Number of Votes Won'].astype(int)

#Print the results
for index, row in results_df.iterrows():
    print(f'{row["Candidate"]} {row["Percent of Votes Won"]:.3f}% ({row["Total Number of Votes Won"]:d})')

#Find the candidate with the most votes
winner = results_df['Candidate'].iloc[results_df['Total Number of Votes Won'].argmax()]

#Print the winner
print('Winner:', winner)