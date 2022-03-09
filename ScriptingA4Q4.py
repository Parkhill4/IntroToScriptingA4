"""
    Question 4:
"""
import random
list = []
for i in range(0,100):
    num = random.randint(0, 20)
    list.append(num)
print(list)
noRepeat = []
for i in list:
    if i not in noRepeat:
        noRepeat.append(i)
print(noRepeat)
