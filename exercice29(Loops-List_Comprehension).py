#List Comprehensions
#Let’s say we have scraped a certain website and gotten these words

#words = ["@coolguy35", "#nofilter", "@kewldawg54", "reply",
#"timestamp", "@matchamom", "follow", "#updog"]

#We want to make a new list, called usernames, that has all of the
#strings in words with an '@' as the first character.
#We know we can do this with a for loop:

words = ["@coolguy35", "#nofilter", "@kewldawg54", "reply", "timestamp",
"@matchamom", "follow", "#updog"]
usernames = []

for word in words:
    if word[0] == '@':
        usernames.append(word)
print(usernames)

messages = [user + " please follow me!" for user in usernames]
print(messages)

#Python has a convenient shorthand to create lists like this with one line:
usernames2 = [word for word in words if word[0] == '@']
print(usernames2)

#We have defined a list heights of visitors to a theme park.
#In order to ride the Topsy Turvy Tumbletron roller coaster,
#you need to be above 161 centimeters. Using a list comprehension,
#create a new list called can_ride_coaster that has every element from
#heights that is greater than 161.

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
#can_ride_coaster = []

#for ride in heights:
#  if ride > 161:
#    can_ride_coaster.append(ride)
#print(can_ride_coaster)

can_ride_coaster = [ride for ride in heights if ride > 161]
print(can_ride_coaster)


fahrenheit = [temp for temp in celsius temp * 9/5 + 32]
