# 5652025  Folio SISAP
import pandas as pd

df = pd.DataFrame([
  ['King Malama', 19, 43],
  ['Eptos One', 17, 40],
],
  columns=['name', 'hourly_wage', 'hours_worked']
)

total_earned = lambda row: ((row.hours_worked - 40) * (row.hourly_wage * 1.5))+(row.hourly_wage * 40) \
  if row.hours_worked > 40 \
  else row.hours_worked * row.hourly_wage

#For add a new colum with a function, we always need the axis=1
df['Salary'] = df.apply(total_earned,axis=1)

print(df)
