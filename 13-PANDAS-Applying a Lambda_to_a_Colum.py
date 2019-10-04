import pandas as pd

df = pd.DataFrame([
  ['JOHN SMITH', 'john.smith@gmail.com'],
  ['Jane Doe', 'jdoe@yahoo.com'],
  ['joe schmo', 'joeschmo@hotmail.com']
],
columns=['Name', 'Email'])


df['Name'] = lambda up: df.Name.apply(upper)
# Add columns here
get_last_name = lambda cut: cut.split()[-1]
df['last_name'] = df.Name.apply(get_last_name)
print(df)
