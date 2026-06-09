# Hardcode everything to bypass user input and test on all tournament data at once

import os
from modules import io as myio
from modules import loadPlayers as playerLoader
from modules import outputRankings as oir
from modules import saveSystem as saveSystem
from modules import matches as matches
from modules import player as player
from modules import saveSystem as saveSystem


def PROCESS_2022_TOURNAMENTS():
    
    # Initialize ranks dictionary
    ranks = {}
    
    # Set K constant
    K = 100

    # Set matchlist path
    matchlist = "data/matchlist.csv"

    # Set ranking output path
    savestate = "data/output.csv"

    # Set datafile paths
    tdata = "data/tdata.csv"
    directory = "data/2022/"

    # Create savestate object
    DB = saveSystem.SaveSystem(matchlist, savestate, tdata)


    


    # Process matches
    # See Tournaments/2022/_TOURNAMENT_LIST.txt for order of tournaments

    # Campbell River
    matchfile = "Tournaments/2022/2022_CRBC.csv"

    # load new players from the new matchfile
    ranks = playerLoader.loadNewPlayers(ranks, directory, matchfile, DB)

    # Update matchlist
    # Add all the matches to the matchlist
    source_file = matchfile
    destination_file = matchlist
    with open(destination_file, "a") as dest:
        dest.write("")
    with open(source_file, "r") as source:
        with open(destination_file, "a") as dest:
            dest.write(source.read())
            dest.write("\n")

    # Update total number of players
    DB.numberPlayers = len(ranks)

    # Process the matches and update the ratings
    ranks = matches.processMatches(ranks, K, matchfile, matchlist, "2022 Campbell River", DB)

    # sort the rankings according to the new ratings
    ranks = oir.sortRankings(ranks)

    # Update the player objects with their new rankings
    oir.updatePlayerRankings(ranks)

    # output the updated player data to the data files
    for player in ranks.values():
        playerLoader.savePlayer(directory, player)

    print("Completed processing 2022 Campbell River tournament.\n\n")

    # Victoria Closed
    matchfile = "Tournaments/2022/2022_VictoriaClosed.csv"

    # Load extant players into ranks, the list of players
    ranks = playerLoader.loadPlayers(ranks, directory)
    # Create new data files for new players and load them into ranks
    ranks = playerLoader.loadNewPlayers(ranks, directory, matchfile, DB)

    # Add all the matches to the matchlist
    source_file = matchfile
    destination_file = matchlist
    with open(destination_file, "a") as dest:
        dest.write("")
    with open(source_file, "r") as source:
        with open(destination_file, "a") as dest:
            dest.write(source.read())

    DB.numberPlayers = len(ranks)

    # Process the matches and update the ratings
    ranks = matches.processMatches(ranks, K, matchfile, matchlist, "2022 Victoria Closed", DB)

    # sort the rankings according to the new ratings
    ranks = oir.sortRankings(ranks)

    # Update the player objects with their new rankings
    oir.updatePlayerRankings(ranks)

    # output the updated player data to the data files
    for player in ranks.values():
        playerLoader.savePlayer(directory, player)

    print("Completed processing 2022 Victoria Closed tournament.\n\n")



    # Provincial Championships
    matchfile = "Tournaments/2022/2022_Provincials.csv"

    # Load extant players into ranks, the list of players
    ranks = playerLoader.loadPlayers(ranks, directory)

    # Create new data files for new players and load them into ranks
    ranks = playerLoader.loadNewPlayers(ranks, directory, matchfile, DB)

    # Add all the matches to the matchlist
    source_file = matchfile
    destination_file = matchlist
    with open(destination_file, "a") as dest:
        dest.write("")
    with open(source_file, "r") as source:
        with open(destination_file, "a") as dest:
            dest.write(source.read())

    DB.numberPlayers = len(ranks)

    # Process the matches and update the ratings
    ranks = matches.processMatches(ranks, K, matchfile, matchlist, "2022 Provincial Championships", DB)

    # sort the rankings according to the new ratings
    ranks = oir.sortRankings(ranks)

    # Update the player objects with their new rankings
    oir.updatePlayerRankings(ranks)

    # output the updated player data to the data files
    for player in ranks.values():
        playerLoader.savePlayer(directory, player)

    print("Completed processing 2022 Provincials.\n\n")


    # New Era Open
    matchfile = "Tournaments/2022/2022_NewEra.csv"

    # Load extant players into ranks, the list of players
    ranks = playerLoader.loadPlayers(ranks, directory)

    # Create new data files for new players and load them into ranks
    ranks = playerLoader.loadNewPlayers(ranks, directory, matchfile, DB)

    # Add all the matches to the matchlist
    source_file = matchfile
    destination_file = matchlist
    with open(destination_file, "a") as dest:
        dest.write("")
    with open(source_file, "r") as source:
        with open(destination_file, "a") as dest:
            dest.write(source.read())

    DB.numberPlayers = len(ranks)

    # Process the matches and update the ratings
    ranks = matches.processMatches(ranks, K, matchfile, matchlist, "2022 New Era Open", DB)

    # sort the rankings according to the new ratings
    ranks = oir.sortRankings(ranks)

    # Update the player objects with their new rankings
    oir.updatePlayerRankings(ranks)

    # output the updated player data to the data files
    for player in ranks.values():
        playerLoader.savePlayer(directory, player)

    print("Completed processing 2022 New Era Open.\n\n")



    # Nanaimo Open
    matchfile = "Tournaments/2022/2022_NanaimoOpen.csv"

    # Load extant players into ranks, the list of players
    ranks = playerLoader.loadPlayers(ranks, directory)

    # Create new data files for new players and load them into ranks
    ranks = playerLoader.loadNewPlayers(ranks, directory, matchfile, DB)

    # Add all the matches to the matchlist
    source_file = matchfile
    destination_file = matchlist
    with open(destination_file, "a") as dest:
        dest.write("")
    with open(source_file, "r") as source:
        with open(destination_file, "a") as dest:
            dest.write(source.read())

    DB.numberPlayers = len(ranks)

    # Process the matches and update the ratings
    ranks = matches.processMatches(ranks, K, matchfile, matchlist, "2022 Nanaimo Open", DB)

    # sort the rankings according to the new ratings
    ranks = oir.sortRankings(ranks)

    # Update the player objects with their new rankings
    oir.updatePlayerRankings(ranks)

    # output the updated player data to the data files
    for player in ranks.values():
        playerLoader.savePlayer(directory, player)

    print("Completed processing 2022 Nanaimo Open.\n\n")



    # Thanksgiving Tournament
    matchfile = "Tournaments/2022/2022_Thanksgiving.csv"

    # Load extant players into ranks, the list of players
    ranks = playerLoader.loadPlayers(ranks, directory)

    # Create new data files for new players and load them into ranks
    ranks = playerLoader.loadNewPlayers(ranks, directory, matchfile, DB)

    # Add all the matches to the matchlist
    source_file = matchfile
    destination_file = matchlist
    with open(destination_file, "a") as dest:
        dest.write("")
    with open(source_file, "r") as source:
        with open(destination_file, "a") as dest:
            dest.write(source.read())

    DB.numberPlayers = len(ranks)

    # Process the matches and update the ratings
    ranks = matches.processMatches(ranks, K, matchfile, matchlist, "2022 C1 Thanksgiving Tournament", DB)

    # sort the rankings according to the new ratings
    ranks = oir.sortRankings(ranks)

    # Update the player objects with their new rankings
    oir.updatePlayerRankings(ranks)

    # output the updated player data to the data files
    for player in ranks.values():
        playerLoader.savePlayer(directory, player)

    print("Completed processing 2022 Thanksgiving Tournament.\n\n")



    # Island Open
    matchfile = "Tournaments/2022/2022_IslandOpen.csv"

    # Load extant players into ranks, the list of players
    ranks = playerLoader.loadPlayers(ranks, directory)

    # Create new data files for new players and load them into ranks
    ranks = playerLoader.loadNewPlayers(ranks, directory, matchfile, DB)

    # Add all the matches to the matchlist
    source_file = matchfile
    destination_file = matchlist
    with open(destination_file, "a") as dest:
        dest.write("")
    with open(source_file, "r") as source:
        with open(destination_file, "a") as dest:
            dest.write(source.read())

    DB.numberPlayers = len(ranks)

    # Process the matches and update the ratings
    ranks = matches.processMatches(ranks, K, matchfile, matchlist, "2022 Island Open", DB)

    # sort the rankings according to the new ratings
    ranks = oir.sortRankings(ranks)

    # Update the player objects with their new rankings
    oir.updatePlayerRankings(ranks)

    # output the updated player data to the data files
    for player in ranks.values():
        playerLoader.savePlayer(directory, player)

    print("Completed processing 2022 Islands.\n\n")
 

    # END OF YEAR UPDATES

    # Update previousAnnualRatings
    ranks = oir.updatePreviousAnnualRatings(ranks)

    # Save progress
    print(f"Outputting final rankings to {savestate}...")
    oir.outputRankingsToCSV(ranks, savestate)
    DB.save()
    print(f"Final rankings have been saved to {savestate}.\n")

    # Print  final rankings
    print("Total number matches processed:", DB.matchesPlayed)
    print("Total number players ranked:", DB.numberPlayers)
    print("Final 2022 Rankings:")
    oir.outputRankingsToConsole(ranks)

    return

PROCESS_2022_TOURNAMENTS()