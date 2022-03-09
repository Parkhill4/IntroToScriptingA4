"""
    Question 2: This program will take a list and find the total
                average, minimum, and maximum
"""
def getTotal():
    total = 0
    for i in range(len(numList)):
        total = total + numList[i]
    return total

def getSmallest():
    numList.sort()
    print("The smallest value in the list is:", numList[0])

def getLargest():
    numList.sort()
    print("The largest value in the list is:", numList[19])

numList = []
for i in range(20):
    number = (int(input("Enter a random number:")))
    numList.append(number)
getSmallest()
getLargest()
print("The total of the list is", getTotal())
print("The average of the list is:",getTotal()/20)
