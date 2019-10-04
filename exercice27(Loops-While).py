#While loop. The while loop performs a set of code
#until some condition is reached.

dog_breeds = ['bulldog', 'dalmation', 'shihtzu', 'poodle', 'collie']

index = 0
while index < len(dog_breeds):
  print(dog_breeds[index])
  index += 1

#You are adding students to a Poetry class, the size of which is capped at 6.
#While the length of the students_in_poetry list is less than 6,
#use .pop() to take a student off the all_students list and add it to t
#he students_in_poetry list

print("--------------------------------------")

all_students = ["Alex", "Briana", "Cheri", "Daniele",
"Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

while len(students_in_poetry) < 6:
    student = all_students.pop()
    students_in_poetry.append(student)
print(students_in_poetry)
