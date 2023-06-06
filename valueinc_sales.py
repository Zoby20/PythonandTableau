#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 24 10:14:41 2023

@author: zohaibahmed
"""

# importing pandas library 
import pandas as pd 

# importing csv file i.e; file_name = pd.read_csv('file.csv') <----- format of read_csv
data = pd.read_csv('transaction.csv')

# this is to tell python that the csv file uses ';' as a separator to seperate the columns
data = pd.read_csv('transaction.csv',sep=';')

#summary of the dataset <------- file_name.info()
data.info()

# defining variables 
#CostPerItem = 11.73
#SellingPricePerItem = 21.11
#NumberOfItemsPurchased = 6


# mathematical operations 
#ProfitPerItem = 21.11-11.73
#ProfitPerItem = SellingPricePerItem - CostPerItem

#ProfitPerTranscation = NumberOfItemsPurchased * ProfitPerItem
#CostPerTranscation = NumberOfItemsPurchased * CostPerItem
#SellingPricePerTransaction = NumberOfItemsPurchased * SellingPricePerItem


# CostPerTransaction Column Calculation 
#CostPerTranscation = NumberOfItemsPurchased * CostPerItem
# How to single out or bring out one column in specific <------ variable = dataframe['column name']

CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
SellingPricePerItem = data['SellingPricePerItem']
data['CostPerTransaction']= CostPerItem * NumberOfItemsPurchased

# Adding a new column to the dataframe
# CostPerTransaction Column Calculation 
#data['CostPerTransaction'] = data['CostPerTransaction'] * data['NumberOfItemsPurchased']

#SalesPerTransaction Column Calculation
data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

# Profit---->Profit = Sales - Cost
# Markup----> Markup = (Sales-Cost)/Cost
# Profit Column Calculation
data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

# Markup Column Calculation
data['Markup'] = (data['SalesPerTransaction'] - data['CostPerTransaction'])/data['CostPerTransaction']

# Using Round() function to reduce decimal points for column 'Markup'
roundmarkup = round(data['Markup'],2)
data['Markup']=roundmarkupt
# or you can run ---> data['Markup'] = round(data['Markup'],2)

# checking the datatype of the columns using 'dtype'
print(data['Day'].dtype)

# converting data types using 'astype'
# converting data fields day,month,year to concatenate the the 3 columns together since they have to be the same datatype
day = data['Day'].astype(str)
year = data['Year'].astype(str)

# combining data fields/columns (Concatenate) 
my_date = day+'-'+data['Month']+'-'+year

# adding new data field/column 'date' and add 'my_date' to this data field
data['date'] = my_date 

# using 'iloc' to view specific columns/rows 
data.iloc[0] #views the row with index = 0 (row 1)
data.iloc[0:3] # first 3 rows
data.iloc[-5:] # last 5 rows
data.head() #  'head() brings in first 5 rows 
data.iloc[:,2] # brings in all rows and 2 columns 
data.iloc[4,2] # brings in 4th row 2nd column

# using split() to split the client keywords field/column 
# i.e; new_var = column.str.split('sep',expand=True)

split_col = data['ClientKeywords'].str.split(',' ,expand=True)

# creating new columns for the split columns in client keywords

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthofContract'] = split_col[2]

# using replace() function to replace the square brackets with empty space in 'clientage' & 'lengthofcontract'

data['ClientAge'] = data['ClientAge'].str.replace('[' ,'')
data['LengthofContract'] = data['LengthofContract'].str.replace(']' ,'')

# using the lower() function to change string from uppercase to lowercase in item description column

data['ItemDescription'] = data['ItemDescription'].str.lower()

# how to merge files
# bringing in new data set 

data2 = pd.read_csv('value_inc_seasons.csv',sep=';')

# merging files 
# i.e; merge_df = pd.merge(df_old,df_new,on='key') on is the common table column between both the datasets


data = pd.merge(data,data2,on='Month')


# dropping columns 
# i.e; df = df.drop['columnname',axis=1]

data = data.drop('ClientKeywords',axis=1)
data = data.drop('Day',axis=1)
data = data.drop(['Month','Year'],axis=1)

# Export data frame into CSV 

data.to_csv('ValueInc_Cleaned.csv',index=False)





