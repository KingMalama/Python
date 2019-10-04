#Larger list
#The function should return the last element of the list that
#contains more elements. If both lists are the same size, then return
#the last element of lst1.

def larger_list(lst1, lst2):
    first = len(lst1)
    second = len(lst2)
    if first > second:
        return (lst1[-1])
    elif second > first:
        return (lst2[-1])
    else: 
        return (lst1[-1])

print(larger_list([4, 10, 2, 5, 6], [-10, 2, 5, 10,7 ,8]))
