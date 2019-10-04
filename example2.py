#Welcome again
def calculate_age(current_year, birth_year):
  age = current_year - birth_year
  return age
#Time to deploy
my_age = calculate_age(2049,1993)
dads_age = calculate_age(2049,1953)
#Time to print babe
print("I am " + str(my_age) + " years old and my dad is " +
 str(dads_age) + " years old")
