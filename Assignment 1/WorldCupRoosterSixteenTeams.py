# Question 10C -
# Randomly assume certain teams win and lose each round and eliminate the losers from the
# preference lists for each team. Can the Gale-Shapley matching algorithm be applied over and over in
# each round (16 teams, 8 teams, 4 teams, 2 teams) to create stable matches? You can answer this with
# code or rhetoric.


import random


def stable_matching(group1, group2):
    teamsInRoundOfEight = []
    teamsInSemiFinal = []
    teamsInFinal = []

    teamsInGroup1 = {
        0: 'England',
        1: 'France',
        2: 'Argentina',
        3: 'Brazil',
        4: 'Mexico',
        5: 'Netherlands',
        6: 'Italy',
        7: 'India',
    }
    teamsInGroup2 = {
        0: 'Portugal',
        1: 'Germany',
        2: 'Uruguay',
        3: 'Denmark',
        4: 'USA',
        5: 'Croatia',
        6: 'Wales',
        7: 'Saudi Arabia',
    }

    # Round of Sixteen at World Cup
    print("Round of 16\n")
    team1Pairings = doStableMatchingOnWorldCupRounds(group1, group2)

    for i, num in enumerate(team1Pairings):
        print(teamsInGroup1[i] + ' vs ' + teamsInGroup2[num])
        teamsPaired = [teamsInGroup1[i], teamsInGroup2[num]]
        winner = random.choice(teamsPaired)
        print("Winner is: " + winner)
        print("===============================\n")
        teamsInRoundOfEight.append(winner)

    random.shuffle(teamsInRoundOfEight)

    # For Quarters
    print("Quarter Finals\n")
    groupOneForQuarters = [teamsInRoundOfEight.pop() for i in range(8) if i < 4]
    groupTwoForQuarters = [teamsInRoundOfEight.pop() for i in range(4)]
    mappingForGroupOneQuarters = {}
    mappingForGroupTwoQuarters = {}

    for index, team in enumerate(groupOneForQuarters):
        mappingForGroupOneQuarters[index] = team

    for index, team in enumerate(groupTwoForQuarters):
        mappingForGroupTwoQuarters[index] = team

    indexes = list(range(4))
    preferencesForGroup1Quarters = []
    preferencesForGroup2Quarters = []
    for x in range(4):
        shuffledList = random.sample(indexes, len(indexes))
        preferencesForGroup1Quarters.append(shuffledList)
        shuffledList2 = random.sample(shuffledList, len(indexes))
        preferencesForGroup2Quarters.append(shuffledList2)

    print("===============================\n")

    team1PairingsForQuarters = doStableMatchingOnWorldCupRounds(preferencesForGroup1Quarters,
                                                                preferencesForGroup2Quarters)
    for i, num in enumerate(team1PairingsForQuarters):
        print(mappingForGroupOneQuarters[i] + ' vs ' + mappingForGroupTwoQuarters[num])
        teamsPaired = [mappingForGroupOneQuarters[i], mappingForGroupTwoQuarters[num]]
        winner = random.choice(teamsPaired)
        print("Winner is: " + winner)
        print("===============================\n")
        teamsInSemiFinal.append(winner)

    # For Semis
    print("Semi Finals\n")
    groupOneForSemis = [teamsInSemiFinal.pop() for i in range(4) if i < 2]
    groupTwoForSemis = [teamsInSemiFinal.pop() for i in range(2)]
    mappingForGroupOneSemis = {}
    mappingForGroupTwoSemis = {}

    for index, team in enumerate(groupOneForSemis):
        mappingForGroupOneSemis[index] = team

    for index, team in enumerate(groupTwoForSemis):
        mappingForGroupTwoSemis[index] = team

    indexes = list(range(2))
    preferencesForGroup1Semis = []
    preferencesForGroup2Semis = []
    for x in range(2):
        shuffledList = random.sample(indexes, len(indexes))
        preferencesForGroup1Semis.append(shuffledList)
        shuffledList2 = random.sample(shuffledList, len(indexes))
        preferencesForGroup2Semis.append(shuffledList2)

    print("\n")

    team1PairingsForSemis = doStableMatchingOnWorldCupRounds(preferencesForGroup1Semis,
                                                             preferencesForGroup2Semis)
    for i, num in enumerate(team1PairingsForSemis):
        print(mappingForGroupOneSemis[i] + ' vs ' + mappingForGroupTwoSemis[num])
        teamsPaired = [mappingForGroupOneSemis[i], mappingForGroupTwoSemis[num]]
        winner = random.choice(teamsPaired)
        print("Winner is: " + winner)
        print("===============================\n")

        teamsInFinal.append(winner)

    print("Finals: " + teamsInFinal[0] + " vs " + teamsInFinal[1])


def doStableMatchingOnWorldCupRounds(group1, group2):
    n = len(group1)
    unPairedTeams = list(range(n))  # [0, 1, 2]
    team1Pairings = [None] * n  # [None, None, None]
    team2Pairings = [None] * n  # [None, None, None]
    proposalsMadeMyTeam1 = [0] * n  # [0, 0, 0]
    while unPairedTeams:
        selectedTeamFromGroup1 = unPairedTeams[0]  # 0
        preferencesOfSelectedTeam = group1[selectedTeamFromGroup1]  # [[0, 1, 2]]
        oppositionTeamFromGroup2 = preferencesOfSelectedTeam[proposalsMadeMyTeam1[selectedTeamFromGroup1]]  # 0 - Brazil
        preferencesOfOppositionTeamGroup2 = group2[oppositionTeamFromGroup2]  # [2, 1, 0]
        currentPairingOfOppositionTeam = team2Pairings[oppositionTeamFromGroup2]

        if currentPairingOfOppositionTeam is None:
            team2Pairings[oppositionTeamFromGroup2] = selectedTeamFromGroup1  # 0
            team1Pairings[selectedTeamFromGroup1] = oppositionTeamFromGroup2  # 0
            proposalsMadeMyTeam1[selectedTeamFromGroup1] += 1  # [1, 0, 0]
            unPairedTeams.pop(0)  # [1, 2]

        else:
            preferenceNumberOfCurrentPairedTeam = preferencesOfOppositionTeamGroup2.index(
                currentPairingOfOppositionTeam)
            preferenceNumberOfSelectedTeamGroup1 = preferencesOfOppositionTeamGroup2.index(selectedTeamFromGroup1)

            if preferenceNumberOfSelectedTeamGroup1 > preferenceNumberOfCurrentPairedTeam:
                team2Pairings[oppositionTeamFromGroup2] = selectedTeamFromGroup1
                team1Pairings[selectedTeamFromGroup1] = oppositionTeamFromGroup2
                proposalsMadeMyTeam1[selectedTeamFromGroup1] += 1
                unPairedTeams.pop(0)
                unPairedTeams.insert(0, currentPairingOfOppositionTeam)
            else:
                proposalsMadeMyTeam1[selectedTeamFromGroup1] += 1
    return team1Pairings


# Driver level code to generate output

# Test Case 1:
superGroup1 = [
    [0, 2, 4, 6, 7, 3, 5, 1],
    [0, 2, 1, 3, 5, 6, 4, 7],
    [1, 2, 3, 4, 7, 6, 5, 0],
    [7, 6, 1, 3, 4, 2, 5, 0],
    [4, 6, 7, 2, 1, 3, 0, 5],
    [3, 7, 4, 1, 2, 0, 5, 6],
    [5, 7, 1, 0, 2, 4, 3, 6],
    [0, 2, 4, 6, 7, 3, 5, 1],
]
superGroup2 = [
    [0, 1, 4, 7, 6, 3, 5, 2],
    [0, 2, 1, 7, 5, 4, 6, 3],
    [3, 2, 1, 7, 4, 6, 5, 0],
    [1, 5, 7, 3, 4, 2, 6, 0],
    [5, 6, 7, 2, 0, 3, 1, 4],
    [2, 6, 4, 1, 3, 5, 0, 7],
    [4, 6, 1, 0, 7, 5, 3, 2],
    [1, 2, 4, 7, 6, 3, 5, 0],
]

stable_matching(superGroup1, superGroup2)


#  Source:
