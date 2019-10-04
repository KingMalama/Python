#Append size
#The function should append the size of lst (inclusive)
#to the end of lst. The function should then return this new list.

def append_size(lst):
    first = len(lst)
    result = lst.append(first)
    return lst

print(append_size([23, 42, 108]))

#Last exercice
#Every three numbers
