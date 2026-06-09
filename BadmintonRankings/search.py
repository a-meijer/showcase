
import os
import csv
from modules import io as myio
from modules import loadPlayers as playerLoader
from modules import outputRankings as oir
from modules import saveSystem as saveSystem
from modules import matches as matches
from modules import player as player
from modules import saveSystem as saveSystem
from pathlib import Path

def search_name(ranks, search_term):
    matches = []

    for player in ranks.values():
        if search_term.lower() in player.name.lower():
            matches.append(player)

    return matches

def search_id(id, ranks):
    for player in ranks.values():
        if(player.id.upper() == id.upper()): 
            print("- Player found with ID", id.upper(), "-")
            print("Name: ", player.name)
            print("Wins: ", player.wins)
            print("Losses: ", player.losses)
            print("Rating: ", player.rating)
            print("Rank: ", player.rank)
            print("Highest Rank: ", player.highestRank)
            print("Previous Rank: ", player.previousAnnualRank)
            print("Highest Rating: ", player.highestRating)
            print("Previous Rating: ", player.previousAnnualRating)
            print("Match History:")
            for row in player.matchHistory:
                print(row)

# Initialize variables
quit = "quit"
command = ""
directory = "data/2022/"
print("Welcome to Player Search!\nDirectory = ",directory)

# Load players into datastructures
print("Loading Player Data. . .")
ranks = {}
ranks = playerLoader.loadPlayers(ranks, directory)
print("Data loaded successfully!\nSearch by name or ID.")

while command != quit:

    print("Type \"quit\" to quit.")
    command = input("> ").strip()

    # Search as ID
    search_id(command, ranks)

    # Search as name
    results = search_name(ranks, command)
    if(len(results) > 0):
        print(f"{len(results)} results searching \"{command}\" by name:")
        for x in results:
            print("Name: ", x.name, "\tID: ", x.id)

    # Continue
    