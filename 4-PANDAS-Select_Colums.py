import pandas as pd

df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)
#One column (Series)
clinic_north1 = df['clinic_north']
#Two or more columns (DataFrame)
clinic_north2 = df[['month','clinic_north']]
#When we select a single column, the result is called a Series.
print(type(clinic_north1))
print(type(df))
print(type(clinic_north2))
print(clinic_north1)
print(clinic_north2)
