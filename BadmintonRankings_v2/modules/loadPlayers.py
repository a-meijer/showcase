'''
methods for loading players from existing rankings and tournament files, and adding them to the ranks dictionary.
'''

import csv
from modules import player
from pathlib import Path

# loadPlayers must be run before saveNewPlayers, or else all the players will be thought to be new
def loadPlayers(ranks, directory):
    filepath = ""

    for filepath in Path(directory).glob("*.csv"):
        ranks[filepath.stem] = loadPlayer(filepath)

    return ranks

def loadPlayer(filepath):
    flag = 0
    with open(filepath, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if flag == 0:
                flag = 1
                id = filepath.stem
                name = row[0]
                wins = int(row[1])
                losses = int(row[2])
                rating = int(row[3])
                rank = row[4]
                highestRank = row[5]
                previousRank = row[6]
                highestRating = int(row[7])
                previousRating = int(row[8])
                addedPlayer = player.Player(name, id, wins, losses, rating, rank, highestRank, previousRank, highestRating, previousRating)
            else:
                match = row[0]
                addedPlayer.matchHistory.append(match)
    return addedPlayer

def loadNewPlayers(ranks, filepath, matchfile, save):
    with open(matchfile, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            playerfile = Path(filepath) / f"{row[2]}.csv"
            playerfile2 = Path(filepath) / f"{row[4]}.csv"
            if not playerfile.exists():
                # Create a new player object
                # name, id, wins, losses, rating, rank, highestRank, previousRank, highestRating, previousRating
                addedPlayer = player.Player(row[1], row[2], 0, 0, 1000, "NR", "NR", "NR", 1000, 1000)  # Default rating of 1000
                # Load the new player into the ranks datastructure
                ranks[row[2]] = addedPlayer
                print(f"Loaded new player {addedPlayer.name} with initial rating {addedPlayer.rating}!")
                # Save the new player to a data file
                with open(playerfile, 'w', newline='') as csvfile:
                    csv_writer = csv.writer(csvfile)
                    csv_writer.writerow([addedPlayer.name, addedPlayer.wins, addedPlayer.losses, addedPlayer.rating])
                print(f"Created new data file for {addedPlayer.name} with filename {playerfile.name}!")
            if not playerfile2.exists():
                # Create a new player object
                # name, id, wins, losses, rating, rank, highestRank, previousRank, highestRating, previousRating
                addedPlayer = player.Player(row[3], row[4], 0, 0, 1000, "NR", "NR", "NR", 1000, 1000)  # Default rating of 1000
                # Load the new player into the ranks datastructure
                ranks[row[4]] = addedPlayer
                print(f"Loaded new player {addedPlayer.name} with initial rating {addedPlayer.rating}!")
                # Save the new player to a data file
                with open(playerfile2, 'w', newline='') as csvfile:
                    csv_writer = csv.writer(csvfile)
                    csv_writer.writerow([addedPlayer.name, addedPlayer.wins, addedPlayer.losses, addedPlayer.rating])
                print(f"Created new data file for {addedPlayer.name} with filename {playerfile.name}!")
    return ranks

def savePlayer(directory, player):
    filepath = Path(directory) / f"{player.id}.csv"
    with open(filepath, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([player.name, player.wins, player.losses, player.rating, player.rank, player.highestRank, player.previousAnnualRank, player.highestRating, player.previousAnnualRating])
        csv_writer.writerows([[match] for match in player.matchHistory])
    return



'''
250
'''



# Deprecated 2025 function
def XloadExistingPlayers(ranks, inputFile):
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

# Deprecated 2025 function
def XloadNewPlayers(ranks, tournamentFile):
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