#Examples of Lambda function
#Create a lambda function named contains_a that takes an input word and
#returns True if the input contains the letter 'a'. Otherwise, return False.

contains_a = lambda word:'a' in word[:]
print contains_a("banana")
print contains_a("apple")
print contains_a("cherry")

#Create a lambda function named long_string that takes an input str and
#returns True if  the string has over 12 characters in it. Otherwise,
#return False.
long_string = lambda word: True if len(word) > 12 else False

print long_string("short")
print long_string("photosynthesis")

#Create a lambda function named ends_in_a that takes an input str and returns
#True if the last character in the string is an a. Otherwise, return False.

ends_in_a = lambda word:str("a") in word[-1]

print ends_in_a("data")
print ends_in_a("aardvark")

#Create a lambda function named double_or_zero that takes an integer named
#num. If num is greater than 10, return double num. Otherwise, return 0.

double_or_zero = lambda num: num*2 if num > 10 else 0

print double_or_zero(15)
print double_or_zero(5)

#random.randint(a,b) will return an integer between a and b (inclusive).
#So, random.randint(5, 8) could return any integer between 5 and 8 including
#both 5 and 8. random.randint(0, 100) could return any integer
#between 0 and 100 including both 0 and 100.

#Write a lambda function that takes an inputted age and either
#returns Welcome to BattleCity! if the user is 13 or older or
#You must be over 13 if they are younger than 13.
#Your lambda function should be called mylambda.

mylambda = lambda age: "Welcome to BattleCity!" if age >= 13 else "You must be over 13"

print(mylambda(14))
