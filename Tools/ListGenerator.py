import random


def listGenerator(n):
    indexes = list(range(n))
    preferenceList1 = []
    preferenceList2 = []
    for x in range(n):
        shuffledList = random.sample(indexes, len(indexes))
        preferenceList1.append(shuffledList)
        shuffledList2 = random.sample(shuffledList, len(indexes))
        preferenceList2.append(shuffledList2)

    print(preferenceList1)
    print(preferenceList2)
    return preferenceList1, preferenceList2


class Tools:
    listGenerator(16)



