#Nested Loops
#Suppose we are in charge of a science class,
#that is split into three project teams:

project_teams = [["Ava", "Samantha", "James"],
 ["Lucille", "Zed"], ["Edgar", "Gabriel"]]

for team in project_teams:
    for student in team:
        print(student)

#We have provided the list sales_data that shows the numbers of different
#flavors of ice cream sold at three different locations of the fictional
#shop, Gilbert and Ilbert’s Scoop Shop. We want to sum up the total number
#of scoops sold.

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0

for location in sales_data:
    print(location)
    for element in location:
        scoops_sold += element
        print(scoops_sold)

#The sum of all elements, equal 96 like the up result
#print(scoops_sold)
