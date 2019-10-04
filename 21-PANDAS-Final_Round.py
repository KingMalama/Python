import pandas as pd
import numpy as np

#Shopyfly Project

ad_clicks = pd.read_csv('ad_clicks.csv')

#Your manager wants to know which ad platform is getting you the most views.
#How many views (i.e., rows of the table) came from each utm_source?

ad_clicks\
    .groupby('utm_source').user_id\
    .count().reset_index()

#If the column ad_click_timestamp is not null, then someone actually clicked
#on the ad that was displayed.
#Create a new column called is_click, which is True if ad_click_timestamp is not
#null and False otherwise.

ad_clicks['is_click'] = ad_clicks\
    .ad_click_timestamp.isnull()

#We want to know the percent of people who clicked on ads from each utm_source.
#Start by grouping by utm_source and is_click and counting the number of
#user_id‘s in each of those groups. Save your answer to the variable clicks_by_source.

clicks_by_source = ad_clicks\
    .groupby(['utm_source','is_click'])\
    .user_id.count().reset_index()

clicks_pivot = clicks_by_source\
    .pivot(index='utm_source',columns='is_click',values='user_id')\
    .reset_index()

#Create a new column in clicks_pivot called percent_clicked which is equal
#to the percent of users who clicked on the ad from each utm_source.

#Was there a difference in click rates for each source?

clicks_pivot['percent_clicked'] = \
    clicks_pivot[True] / \
    (clicks_pivot[True] + \
    clicks_pivot[False]) * 100

#The column experimental_group tells us whether the user was shown Ad A or Ad B.
#Were approximately the same number of people shown both adds?

#ad_clicks\
#    .groupby('experimental_group')\
#    .user_id.count()

#Using the column is_click that we defined earlier, check to see if a greater
#percentage of users clicked on Ad A or Ad B.

ad_clicks\
    .groupby(['experimental_group','is_click'])\
    .user_id.count()


#The Product Manager for the A/B test thinks that the clicks might have changed
#by day of the week.

a_clicks = ad_clicks[\
    ad_clicks.experimental_group == 'A']

b_clicks = ad_clicks[\
    ad_clicks.experimental_group == 'B']


#For each group (a_clicks and b_clicks), calculate the percent of users who
#clicked on the ad by day.

#First the A
a_clicks_by_day = a_clicks\
    .groupby(['day','is_click'])\
    .user_id.count().reset_index()

a_clicks_pivot = a_clicks_by_day\
    .pivot(index='day',columns='is_click',values='user_id')\
    .reset_index()

a_clicks_pivot['percent_clicked'] = \
    a_clicks_pivot[True] / \
    (a_clicks_pivot[True] + \
    a_clicks_pivot[False]) * 100

#Let's do the B Ad
b_clicks_by_day = b_clicks\
    .groupby(['day','is_click'])\
    .user_id.count().reset_index()

b_clicks_pivot = b_clicks_by_day\
    .pivot(index='day',columns='is_click',values='user_id')\
    .reset_index()

b_clicks_pivot['percent_clicked'] = \
    b_clicks_pivot[True] / \
    (b_clicks_pivot[True] + \
    b_clicks_pivot[False]) * 100

#RESULTS
print('----------------------------------------------------------')
print('Results Ad A')
print('----------------------------------------------------------')
print(a_clicks_pivot)
print('----------------------------------------------------------')
print('Results Ad B')
print('----------------------------------------------------------')
print(b_clicks_pivot)

#Do you recommend that your company use Ad A or Ad B?
# The answer is the B Ad
