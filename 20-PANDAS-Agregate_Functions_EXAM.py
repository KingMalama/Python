import pandas as pd
import numpy as np

user_visits = pd.read_csv('.\page_visits.csv')

#The column utm_source contains information about how users got to ShoeFly’s
#homepage. For instance, if utm_source = Facebook, then the user came to
#ShoeFly by clicking on an ad on Facebook.com.

#Use a groupby statement to calculate how many visits came from each of
#the different sources. Save your answer to the variable click_source.

click_source = user_visits.groupby('utm_source').id.count().reset_index()
print(click_source)

print('---------------------------------')

click_source_by_month = user_visits.groupby(['utm_source','month'])['id'].count().reset_index()
print(click_source_by_month)

print('---------------------------------')
#The head of Marketing is complaining that this table is hard to read.
#Use pivot to create a pivot table where the rows are utm_source and
#the columns are month.
#Save your results to the variable click_source_by_month_pivot.

click_source_by_month_pivot = click_source_by_month.pivot(columns='month',index='utm_source',values='id').rest_index()
print(click_source_by_month_pivot)
