"""
    Question 3: This program will create a dictionary and store
                the numbers square in the dictionary
"""
number = int(input("Enter any number: "))
dict = dict()

for i in range(1, number + 1):
    dict[i] = i * i
print(dict)
