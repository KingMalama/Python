import pandas as pd

df = pd.DataFrame([
[54791,'Frances','Palmer', 'female','FrancesPalmer50@gmail.com','clogs','leather','red'],
[53450,'Gabriel','Porter','male','GabrielPorter24@gmail.com','sandles','fabric','white'],
[91987,'Janice','Hicks','female','Janice.Hicks@gmail.com','ballet flats','faux-leather','black'],
[14437,'Thomas','Banks','male','TJ5470@gmail.com','boots','leather','brown'],
[79357,'Julie','Marsh','female','JulieMarsh59@gmail.com','wedges','faux-leather','navy'],
[62083,'Theodor','Connoer','male','Conoer23@gmail.com','clogs','fabric','brown']
],
columns = ['id', 'first_name', 'last_name', 'gender', 'email', 'shoe_type', 'shoe_material','shoe_color']
)

#Many of our customers want to buy vegan shoes
#(shoes made from materials that do not come from animals).
#Add a new column called shoe_source, which is vegan if the materials
#is not leather and animal otherwise.

df['shoe_source'] = df.shoe_material.apply(lambda source: 'animal' if source == 'leather' else 'vegan')

#Our marketing department wants to send out an email to each customer.
#Using the columns last_name and gender create a column called salutation
#which contains Dear Mr. <last_name> for men and Dear Ms. <last_name> for women.

df['saltation'] = df.apply(lambda x: 'Mr.'+ x['last_name'] \
  if x['gender'] == 'male' \
  else 'Mra.'+ x['last_name'], axis=1)

print(df)
