#(MY CODE) Write your lots_of_math function here:
def lots_of_math(a,b,c,d):
  first = a+b
  second = c-d
  third = first * second
  fourth = third % a
  return first,second,third,fourth
# Uncomment these function calls to test your lots_of_math function:
#print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
print(lots_of_math(1,2,3,4))
#print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0
print(lots_of_math(1,1,1,1))

#CODECADEMY
# Write your lots_of_math function here:
def lots_of_math(a, b, c, d):
  first = a+b
  second = c-d
  third = first*second
  fourth = third%a
  print(first)
  print(second)
  print(third)
  return fourth

# Uncomment these function calls to test your lots_of_math function:
print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0