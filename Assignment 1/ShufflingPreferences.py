import random


def doStableMatchingOnWorldCupRounds(group1, group2):
    n = len(group1)
    numberOfStableMatches = 0
    for x in range(1000):
        random.shuffle(group1)
        random.shuffle(group2)
        unPairedTeams = list(range(n))  # [0, 1, 2]
        team1Pairings = [None] * n  # [None, None, None]
        team2Pairings = [None] * n  # [None, None, None]
        proposalsMadeMyTeam1 = [0] * n  # [0, 0, 0]
        while unPairedTeams:
            selectedTeamFromGroup1 = unPairedTeams[0]  # 0
            preferencesOfSelectedTeam = group1[selectedTeamFromGroup1]  # [[0, 1, 2]]
            oppositionTeamFromGroup2 = preferencesOfSelectedTeam[
                proposalsMadeMyTeam1[selectedTeamFromGroup1]]  # 0 - Brazil
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

        if None not in team1Pairings:
            numberOfStableMatches += 1

    percentageOfSuccessfulMatches = (numberOfStableMatches/1000) * 100
    print("Percentage of successful matches :", percentageOfSuccessfulMatches, "%")



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

doStableMatchingOnWorldCupRounds(superGroup1, superGroup2)