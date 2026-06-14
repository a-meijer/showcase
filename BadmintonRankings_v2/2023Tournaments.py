# Hardcode everything to bypass user input and test on all tournament data at once

import os
from modules import io as myio
from modules import loadPlayers as playerLoader
from modules import outputRankings as oir
from modules import saveSystem as saveSystem
from modules import matches as matches
from modules import player as player
from modules import saveSystem as saveSystem

def PROCESS_2023_TOURNAMENTS():
    
    # Initialize ranks dictionary
    ranks = {}
    
    # Set K constant
    K = 100

    # Set matchlist path
    matchlist = "data/matchlist.csv"

    # Set ranking path
    savestate = "data/output.csv"

    # Set datafile path
    tdata = "data/tdata.csv"
    directory = "data/2022/"

    # Create savestate object
    DB = saveSystem.SaveSystem(matchlist, savestate, tdata)


    ''' Process matches '''
    # Add these in the correct chronological order
    # See Tournaments/2023/_TOURNAMENT_LIST.txt for order of tournaments

    matchfiles = []
    tnames = []

    # New Year's Tournament 
    matchfiles.append("Tournaments/2023/2023_C1NY.csv")
    tnames.append("2023 New Year's Tournament")
    # BC Senior Elite
    matchfiles.append("Tournaments/2023/2023_SeniorElite.csv")
    tnames.append("2023 BC Senior Elite")
    # Campbell River
    matchfiles.append("Tournaments/2023/2023_CRBC.csv")
    tnames.append("2023 Campbell River")
    # Kelowna Adult Open
    matchfiles.append("Tournaments/2023/2023_KelownaAdult.csv")
    tnames.append("2023 Kelowna Adult Open")
    # Wing's-GHS Tournament
    matchfiles.append("Tournaments/2023/2023_Wings.csv")
    tnames.append("2023 Wing's-GHS Tournament")
    # Jack Underhill
    matchfiles.append("Tournaments/2023/2023_JackUnderhill.csv")
    tnames.append("2023 Jack Underhill")

    
    for matchfile, tname in zip(matchfiles,tnames):

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
        ranks = matches.processMatches(ranks, K, matchfile, matchlist, tname, DB)

        # sort the rankings according to the new ratings
        ranks = oir.sortRankings(ranks)

        # Update the player objects with their new rankings
        oir.updatePlayerRankings(ranks)

        # output the updated player data to the data files
        for player in ranks.values():
            playerLoader.savePlayer(directory, player)

        print("Finished processing",tname,"\n")


    # Provincial Championship

    # New Era Open

    # Nanaimo Open

    # Thanksgiving Tournament

    # Island Open



    # END OF YEAR UPDATES

    # Update previousAnnualRatings
    ranks = oir.updatePreviousAnnual(ranks)

    # Save progress
    print(f"Outputting final rankings to {savestate}...")
    oir.outputRankingsToCSV(ranks, savestate)
    DB.save()
    print(f"Final rankings have been saved to {savestate}.\n")

    # Print  final rankings
    print("Total number matches processed:", DB.matchesPlayed)
    print("Total number players ranked:", DB.numberPlayers)
    print("Final 2023 Rankings:")
    oir.outputRankingsToConsole(ranks)

    return

PROCESS_2023_TOURNAMENTS()