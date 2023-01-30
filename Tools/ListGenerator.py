import random


def listGenerator(n):
    indexes = list(range(n))
    preferencesForGroup1Quarters = []
    preferencesForGroup2Quarters = []
    for x in range(n):
        shuffledList = random.sample(indexes, len(indexes))
        preferencesForGroup1Quarters.append(shuffledList)
        shuffledList2 = random.sample(shuffledList, len(indexes))
        preferencesForGroup2Quarters.append(shuffledList2)

    print(preferencesForGroup1Quarters)
    print(preferencesForGroup2Quarters)


listGenerator(16)