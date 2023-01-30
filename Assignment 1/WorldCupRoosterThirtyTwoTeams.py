import time


def stable_matching(group1, group2):
    startTime = time.time()
    teamsInGroup1 = {
        0: 'England',
        1: 'France',
        2: 'Argentina',
        3: 'Brazil',
        4: 'Mexico',
        5: 'Netherlands',
        6: 'Italy',
        7: 'Chile',
        8: 'Canada',
        9: 'Australia',
        10: 'Japan',
        11: 'Belgium',
        12: 'Northern Ireland',
        13: 'Iran',
        14: 'Ghana',
        15: 'Czech Republic'
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
        8: 'Canada',
        9: 'Morocco',
        10: 'Egypt',
        11: 'Qatar',
        12: 'Ecuador',
        13: 'Poland',
        14: 'Serbia',
        15: 'Ukraine'
    }
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
    for i, num in enumerate(team1Pairings):
        print(teamsInGroup1[i] + ' vs ' + teamsInGroup2[num])

    endTime = time.time()
    print(f"\nTime taken for creating a fixture list with 32 teams: \t: {(endTime-startTime)*10**3:.03f}ms")


# Driver level code to generate output

# Test Case 1:
superGroup1 = [
    [12, 5, 0, 2, 3, 1, 4, 15, 11, 8, 7, 10, 6, 9, 13, 14],
    [7, 2, 15, 8, 0, 6, 5, 10, 3, 4, 12, 9, 11, 1, 14, 13],
    [1, 5, 0, 12, 7, 2, 15, 9, 4, 11, 8, 6, 14, 10, 13, 3],
    [5, 15, 0, 2, 4, 1, 7, 3, 12, 6, 8, 9, 11, 10, 14, 13],
    [8, 13, 1, 4, 9, 5, 2, 10, 12, 15, 7, 11, 3, 0, 6, 14],
    [0, 15, 11, 1, 8, 9, 10, 6, 5, 13, 12, 14, 3, 7, 2, 4],
    [1, 12, 3, 2, 11, 14, 15, 8, 4, 9, 7, 0, 13, 10, 6, 5],
    [9, 5, 14, 4, 12, 10, 11, 3, 1, 0, 6, 7, 8, 2, 15, 13],
    [0, 5, 1, 4, 8, 7, 12, 6, 15, 13, 9, 2, 10, 3, 11, 14],
    [4, 9, 8, 10, 5, 13, 15, 1, 12, 3, 6, 7, 14, 11, 0, 2],
    [6, 3, 15, 8, 1, 4, 10, 7, 13, 12, 14, 9, 11, 5, 2, 0],
    [7, 13, 2, 4, 8, 14, 11, 15, 3, 5, 9, 12, 10, 0, 1, 6],
    [7, 5, 11, 8, 4, 0, 10, 14, 1, 9, 2, 15, 13, 3, 6, 12],
    [12, 8, 7, 5, 4, 14, 15, 10, 6, 9, 3, 1, 13, 2, 0, 11],
    [12, 2, 13, 7, 4, 5, 0, 1, 9, 15, 10, 11, 6, 8, 14, 3],
    [15, 6, 14, 11, 7, 1, 5, 3, 9, 2, 4, 10, 8, 12, 13, 0]
]

superGroup2 = [
    [10, 0, 7, 2, 14, 9, 15, 12, 13, 3, 8, 6, 5, 11, 4, 1],
    [1, 11, 12, 8, 14, 4, 9, 5, 0, 7, 3, 15, 6, 10, 13, 2],
    [0, 10, 1, 2, 4, 13, 14, 5, 9, 7, 12, 6, 3, 15, 11, 8],
    [0, 1, 12, 6, 7, 5, 10, 15, 2, 9, 4, 13, 14, 8, 3, 11],
    [11, 4, 5, 1, 10, 12, 8, 2, 0, 15, 9, 3, 7, 13, 6, 14],
    [0, 2, 11, 4, 10, 9, 5, 13, 7, 6, 1, 14, 12, 15, 3, 8],
    [11, 4, 10, 12, 0, 8, 3, 5, 9, 1, 6, 7, 13, 2, 14, 15],
    [1, 9, 14, 5, 7, 12, 15, 0, 6, 11, 2, 4, 8, 3, 13, 10],
    [13, 2, 10, 9, 5, 15, 11, 14, 4, 7, 6, 12, 1, 3, 8, 0],
    [3, 7, 8, 9, 14, 13, 1, 2, 10, 11, 15, 5, 0, 4, 6, 12],
    [4, 0, 8, 14, 10, 13, 7, 9, 12, 2, 11, 15, 1, 6, 5, 3],
    [7, 13, 6, 1, 2, 8, 15, 10, 3, 5, 12, 11, 0, 9, 4, 14],
    [11, 9, 3, 6, 0, 12, 5, 10, 4, 14, 2, 8, 13, 1, 15, 7],
    [12, 0, 9, 1, 7, 10, 8, 13, 6, 14, 15, 11, 4, 3, 2, 5],
    [2, 0, 3, 10, 4, 15, 13, 11, 8, 1, 12, 14, 6, 9, 7, 5],
    [11, 14, 9, 1, 15, 6, 10, 2, 5, 7, 3, 0, 12, 4, 8, 13]
]

stable_matching(superGroup1, superGroup2)

#  Source:
