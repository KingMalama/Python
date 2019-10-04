import pandas as pd
import numpy as np

orders = pd.read_csv('.\ShoeFly.csv')

shoe_counts = orders.groupby(['shoe_type', 'shoe_color']).id.count().reset_index()

shoe_counts_pivot = shoe_counts.pivot(columns='shoe_color',index='shoe_type',values='id').reset_index()

print(shoe_counts_pivot)
