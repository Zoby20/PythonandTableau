#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 11:18:41 2023

@author: zohaibahmed
"""

# import pandas
# reading excel or xlsx files using 'read_excel'
#importing vaderSentiment for sentiment analysis



import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

data = pd.read_excel('articles.xlsx')

# getting a statistical summary on the data using describe()
data.describe()

# summary of dataset using info()
data.info()
# counting the number of articles per source using groupby()
# syntax of groupby() -> df.group(['column_to_group'])['column_to_count'].count()

data.groupby(['source_id'])['article_id'].count()

# Counting the number of reactions per source 
data.groupby(['source_id'])['engagement_reaction_count'].sum()

# dropping engagement_comment_plugin_count column 
data = data.drop('engagement_comment_plugin_count',axis=1)

# creating a keyword flag

#keyword = "crash"

# creating a for loop for the 'title' column where it will loop through the whole column and find the keyword 'crash'.
# declaring column name before for loop
#length = len(data)
#keyword_flag=[]
#for x in range(0,length):
 #   heading = data['title'][x]
    
    
  #  if keyword in heading:
       # flag = 1
   # else:
    #    flag = 0
  
        # 'append' will add all the for loop values in this new column
    #keyword_flag.append(flag)




# creating a function for a user to enter keyword which then will loop through the "title" column and flag it either 1 or 0 
def keywordflag(keyword):
    length = len(data)
    keyword_flag = []
    for x in range(0,length):
        heading = data['title'][x]
        try:
            if keyword in heading:
                flag = 1
            else:
                flag = 0
        except:
            flag = 0
        keyword_flag.append(flag)
    return keyword_flag
        
        
keywordflag = keywordflag("murder")

# creating a new column in the data dataframe after converting datatype from list to series

data['keyword_flag'] = pd.Series(keywordflag)


#SentimentIntensityAnalyzer 

sent_int = SentimentIntensityAnalyzer()

text = data['title'][16]
sent = sent_int.polarity_scores(text)

neg = sent['neg']
pos = sent['pos']
neu = sent['neu']

# adding a for loop to extract sentiment per title 
title_neg_sentiment=[]
title_pos_sentiment=[]
title_neu_sentiment=[]
length = len(data)

for x in range(0,length):
    try:
        text = data['title'][x]
        sent_int = SentimentIntensityAnalyzer()
        sent = sent_int.polarity_scores(text)
        neg = sent['neg']
        pos = sent['pos']
        neu = sent['neu']
    except:
        neg = 0
        pos = 0
        neu = 0
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)
# converting list to series data type    
title_neg_sentiment = pd.Series(title_neg_sentiment)
title_pos_sentiment = pd.Series(title_pos_sentiment)
title_neu_sentiment = pd.Series(title_neu_sentiment)

# creating 3 new columns for neg,pos,neu
data['title_neg_sentiment'] = title_neg_sentiment
data['title_pos_sentiment'] = title_pos_sentiment
data['title_neu_sentiment'] = title_neu_sentiment


# writing the data to excel

data.to_excel('blogme_clean.xlsx',sheet_name='blogmedata',index=False)


    
    







