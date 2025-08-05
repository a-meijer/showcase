'''
For a specific Tournament Subdirectory,
This program produces initialRankings.csv given playerData.csv and the match data CSV that shares the same name as the directory.
'''

import csv
from modules import player

def loadExistingPlayers(ranks, inputFile):
    numPlayersAdded = 0
    with open(inputFile, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            rating = int(row[0])
            name = row[1]
            id = row[2]
            wins = int(row[3])
            losses = int(row[4])
            addedPlayer = player.Player(name, id, wins, losses, rating)
            ranks[id] = addedPlayer
            numPlayersAdded += 1

    print(f"Number of players added from existing rankings: {numPlayersAdded}")
    return ranks

def loadNewPlayers(ranks, tournamentFile):
    numPlayersAdded = 0
    with open(tournamentFile, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row[2] not in ranks:
                addedPlayer = player.Player(row[1], row[2], 0, 0, 1000)  # Default rating of 1000
                ranks[row[2]] = addedPlayer
                numPlayersAdded += 1
                print(f"Added new player {addedPlayer.name} with initial rating {addedPlayer.rating}!")
            if row[4] not in ranks:
                addedPlayer = player.Player(row[3], row[4], 0, 0, 1000)  # Default rating of 1500
                ranks[row[4]] = addedPlayer
                numPlayersAdded += 1
                print(f"Added new player {addedPlayer.name} with initial rating {addedPlayer.rating}!")
    print(f"Number of new players added from tournament file: {numPlayersAdded}")
    return ranks