#Len's Slice Pizza project
#Define the lists (menu)
toppings = ['pepperoni', 'pineapple',
'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']

prices = [2, 6, 1, 3, 2, 7, 2]

#How many pizza's toppings we got?
num_pizzas = (len(toppings))
print("We sell " + str(num_pizzas) +" different kind of pizza!")

#Combine the lists (menu)
pizzas = list(zip(prices, toppings))
print(pizzas)
#Sort pizzas with the lowest prices at the start of the list.
sorted_pizzas = sorted(pizzas)
print(sorted_pizzas)
#The cheapest pizza
cheapest_pizza = sorted_pizzas[0]
print("The cheapest pizza is: "+str(cheapest_pizza))
#The most expensive pizza!
priciest_pizza = sorted_pizzas[-1]
print("The most expensive pizza is: "+str(priciest_pizza))
#The 3 cheapest pizzas.
three_cheapest = sorted_pizzas[:3]
print(three_cheapest)
#2 dolars cost
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
