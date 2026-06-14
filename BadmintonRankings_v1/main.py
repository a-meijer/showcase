# File: BadmintonRankings/src/main.py
# Default Input File: Ratings.csv
# Default Output File: outputRatings.csv
# Default Tourmament File: Tournaments/2022_ProvincialChampionship/2022_ProvincialChampionship.csv

import os
from modules import io as myio
from modules import createInitialRankings as cir
from modules import outputRankings as oir
from modules import matches as matches

# Initialize ranks dictionary
ranks = {}
# Set K constant
K = 100

# Get Filenames from user IO
myio.welcome()
inputFile = myio.get_input_filename()
outputFile = myio.get_output_filename()
tournamentFile, tournamentName = myio.get_tournament_filename()


print("File Selection Complete!")
print(f"Input File: {inputFile}")
print(f"Output File: {outputFile}")
print(f"Tournament File: {tournamentFile}")
print(f"Tournament Name: {tournamentName}\n")
print("Continue? (y/n)")
continueProgram = input().strip().lower() == 'y'
if not continueProgram:
    print("Exiting the program.")
    exit()

# Input Ranks
# Rankings.csv is a list of players.
# Each player in Rankings.csv needs to be loaded into a player object.
print(f"Creating player dictionary from {inputFile}...")
ranks = cir.loadExistingPlayers(ranks, inputFile)

# Load new players from tournament file
print(f"Adding new players from {tournamentFile}...")
ranks = cir.loadNewPlayers(ranks, tournamentFile)

# Output Initial Rankings
ranks = oir.sortRankings(ranks)
print("Initial Rankings:")
oir.outputRankingsToConsole(ranks)

# Match Processing
ranks = matches.processMatches(ranks, K, tournamentFile, tournamentName)
print("Match processing complete!\n")

# Output Final Rankings
ranks = oir.sortRankings(ranks)
print("Final Rankings:")
oir.outputRankingsToConsole(ranks)

# Output to CSV
print(f"Outputting final rankings to {outputFile}...")
oir.outputRankingsToCSV(ranks, outputFile)
print(f"Final rankings have been saved to {outputFile}.\n")