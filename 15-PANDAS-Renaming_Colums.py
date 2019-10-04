import pandas as pd

df = pd.DataFrame([
  ['King Malama', 19, 43],
  ['Eptos One', 17, 40],
],
  columns=['name', 'hourly_wage', 'hours_worked']
)
#Rename all columns
df.columns = ['Nickname', 'Hourly_wage', 'Hours_worked']

#Rename just one column
df.rename(columns = {'Nickname':'NICKNAME'}, inplace=True)

print(df)
