#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 13:28:43 2023

@author: zohaibahmed
"""

# importing json in python
# importing pandas 
# importing numpy 
# importing matplotlib

import json
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

# method 1 : to read and load json data 
json_file = open('loan_data_json.json')
data = json.load(json_file)

# method 2 : to read and load json data
#with open('loan_data_json.json') as json_file:
    #data = json.load(json_file)
    

# transforming json file which is in a list format to a dataframe
# DataFrame() - transforms list to dataframe format
loandata = pd.DataFrame(data)   

#  unique() - finding unique values for the 'purpose' column
loandata['purpose'].unique()

# describe() - this function returns statistical info about the dataset
loandata.describe()

# using describe() for a specific column 
loandata['dti'].describe()

# exp() - function converts the log value into a exponent
# We are going to create a new column where we will apply the Exp() function and convert the log into exponents to get the yearly annual income in the "log.annual.inc" column

income = np.exp(loandata['log.annual.inc'])
loandata['annual_income'] = income 

# creating if/elif/else conditions for FICO score to categorize them

fico = 350

# fico >= 300 and < 400: 'Very Poor'
# fico >= 400 and ficoscore < 600: 'Poor' 
# fico >= 601 and ficoscore < 660: 'Fair' 
# fico >= 660 and ficoscore < 780: 'Good' 
# fico >=780: 'Excellent'    

if fico >= 300 and fico < 400:
    ficocat = 'Very Poor'
elif fico >= 400 and fico < 600:
    ficocat = 'Poor'
elif fico >= 601 and fico < 660:
    ficocat = 'Fair'
elif fico >= 660 and fico < 700:
    ficocat = 'Good'
elif fico >= 700:
    ficocat = 'Excellent'
else:
    ficocat = 'Unknown'
print(ficocat)


# Applying FOR loops with loan data with if/elif/else statements and adding it to new column 'ficocat'
# len() - function finds the the length of the dataset
# try() & except() - functions is used to catch any errors in the code and customize the error code
length = len(loandata)
ficocat = []
for x in range(0,length):
    category = loandata['fico'][x]
    try:
        
    
        
        if category >= 300 and category < 400:
            cat = 'Very Poor'
        elif category >= 400 and category < 600:
            cat = 'Poor'
        elif category >= 601 and category < 660:
            cat = 'Fair'
        elif category >= 660 and category < 700:
            cat = 'Good'
        elif category >= 700:
            cat = 'Excellent'
        else:
           cat = 'Unknown'
    except: cat = 'Unknown'

    ficocat.append(cat)
        
# Series datatype is a column in a dataframe, so we have to convert 'ficocat' which is a list type right now to a 'series' type to be stored in a dataframe
ficocat = pd.Series(ficocat)

# Creating new column 'fico.category' into our loandata dataframe
loandata['fico.category'] = ficocat 


# 'df.loc' - is used to create a new column based on some conditon
#  Syntax -> df.loc[df[column_name]condition,new_column_name] = 'value if the condition is met'

# for 'int.rate' column, we'll create a new column where the condition weill be: when rate > 0.12 then high, else low.
# Note -> This is also another method of creating new columns based on condition, similarly we can use for loops for column creation

loandata.loc[loandata['int.rate'] > 0.12,'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12,'int.rate.type'] = 'Low'


# Analysis -> Number of loans/rows by 'fico.category' column 
# groupby() - function groups a particular column 
# size() - function is a count of rows 
catplot = loandata.groupby (['fico.category']).size()
# 'plot' , 'bar()' is used to plot the points into a bar chart
# 'show()' - is used to display the chart 
catplot.plot.bar(color='green', width = 0.5)
plt.show()

# Analysis -> Number of rows by 'purpose' column
purposeplot = loandata.groupby(['purpose']).size()

purposeplot.plot.bar()
plt.show()

# Scatterplots 

xpoint = loandata['dti']
ypoint = loandata['annual_income']
plt.scatter(xpoint,ypoint,color='red')
plt.show()


# Export data frame into CSV 

loandata.to_csv('loan_cleaned.csv',index=True)























