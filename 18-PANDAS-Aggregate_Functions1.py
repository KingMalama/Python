import pandas as pd
import numpy as np

df = pd.read_csv('.\ShoeFly.csv')

pricey_shoes = df.groupby('shoe_type').price.max()

print(pricey_shoes)
#With this command we can see the type of the result, in this case we see a Series
print(type(pricey_shoes))

#Now if we add the following code, we can see the change SERIES BY DataFrame
pricey_shoes2 = df.groupby('shoe_type').price.max().reset_index()
print(pricey_shoes2)
print(type(pricey_shoes2))

print('------------------------------------')

#Let’s calculate the 25th percentile for shoe price for each shoe_color
#to help Marketing decide if we have enough cheap shoes on sale.
#Save the data to the variable cheap_shoes.
cheap_shoes = df.groupby('shoe_color').price.apply(lambda x: np.percentile(x,25)).reset_index()
print(cheap_shoes)

#Create a DataFrame with the total number of shoes of each
#shoe_type/shoe_color combination purchased. Save it to the
#variable shoe_counts.

#You should be able to do this using groupby and count().

#Note: When we’re using count(), it doesn’t really matter which column
#we perform the calculation on. You should use id in this example, but we
#would get the same answer if we used shoe_type or last_name.

#Remember to use reset_index() at the end of your code!
print('--------------------------------------')
shoe_counts = df.groupby(['shoe_type','shoe_color'])['id'].count().reset_index()
print(shoe_counts)

print('--------------------------------------')
example2= df.groupby('shoe_color').id\
      .count().reset_index()
print(example2)
