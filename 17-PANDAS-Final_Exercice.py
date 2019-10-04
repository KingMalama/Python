import pandas as pd

#Data for all of the locations of Petal Power is in
#the file inventory.csv. Load the data into a
#DataFrame called inventory.

df = pd.read_csv('Python\APetals.csv')

#Inspect the first 10 rows of inventory.
#10 rows represent data from your Staten Island location.
#Select these rows and save them to staten_island.

#staten_island=df.head(10)

#print(staten_island)

#Select the column product_description from staten_island
#and save it to the variable product_request.
#product_request = df.product_description[df.location.isin(['Staten Island'])]
#print(product_request)

#Select all rows where location is equal to Brooklyn and
#product_type is equal to seeds and save them to the variable
#seed_request

#seed_request = df[df.location.isin(['Brooklyn'])&df.product_type .isin(['seeds'])]
#print(seed_request)

#Add a column to inventory called in_stock which is True if quantity
#is greater than 0 and False if quantity equals 0.

#df['in_stock'] = df.apply(lambda x: \
#    'True' if x['quantity'] > 0
#      else 'False', axis=1)

#Create a column called total_value that is
#equal to price multiplied by quantity.

#Remember we can use:

#df.quantity * df.price or df['price']*df['quantity']
#df['total_value'] = df.quantity * df['price']

#The following lambda function combines product_type and
#product_description into a single string:

#combine_lambda = lambda row: \
#    '{} - {}'.format(row.product_type,
#                     row.product_description)
#

#Using combine_lambda, create a new column in inventory called
#full_description that has the complete description of each product.

#df['full_description'] = df.apply(combine_lambda,axis=1)

print(df.head(5))
