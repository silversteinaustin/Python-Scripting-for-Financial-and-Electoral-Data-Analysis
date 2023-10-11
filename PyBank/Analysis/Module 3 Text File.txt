import pandas as pd

#Create file path across directory
import os

#import the csv file
import csv

csvpath = os.path.join('Resources','budget_data.csv')

#Read the CSV file into a Pandas DataFrame
df = pd.read_csv(csvpath)

#Calculate the total number of months in the data set
total_months = len(df['Date'].unique())

#Print results
print('The total number of months in the dataset is:', total_months)

#Calculate the net total amount of "Profit/Losses" over the entire period
net_total_p_l= df['Profit/Losses'].sum()

#Print the P/L Result denoted in terms of money
print(f'The net amount of "Profit/Losses" over the entire period is:${net_total_p_l:,.2f}')

#Calculate the changes in "Profits/Losses" over the entire period
changes_in_p_l = df['Profit/Losses'].diff()

#Calculate the average of the changes in "Profits/Losses" over the entire period
avg_change_in_p_l = changes_in_p_l.mean()

#print('The changes in "Profit/Losses" over the entire period are:', changes_in_p_l)
print('The average of the changes in "Profit/Losses" over the entire period is', avg_change_in_p_l)

#Find the greatest increase in profits (date and amount) over the entire period
greatest_increase_in_p_l = changes_in_p_l.max()
greatest_increase_in_p_l_date = df.loc[changes_in_p_l == greatest_increase_in_p_l, 'Date'].iloc[0]

#Print the results 
print(f'The greatest increase in profits over the entire period is: ${greatest_increase_in_p_l:,.2f} on {greatest_increase_in_p_l_date}')

#Find the greatest decrease in profits (date and amount) over the entire period
greatest_decrease_in_p_l = changes_in_p_l.min()
greatest_decrease_in_p_l_date = df.loc[changes_in_p_l == greatest_decrease_in_p_l, 'Date'].iloc[0]

#Print the results 
print(f'The greatest decrease in profits over the entire period is: ${greatest_decrease_in_p_l:,.2f} on {greatest_decrease_in_p_l_date}')