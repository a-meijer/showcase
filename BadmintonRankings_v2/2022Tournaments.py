# Hardcode everything to bypass user input and test on all tournament data at once

import os
from modules import io as myio
from modules import loadPlayers as playerLoader
from modules import saveSystem as saveSystem
from modules import matches as matches
from modules import player as player
from modules import saveSystem as saveSystem


def PROCESS_2022_TOURNAMENTS():
    
    # Initialize ranks dictionary
    ranks = {}

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
    ranks = matches.processMatches(ranks, matchfile, matchlist, "2022 Campbell River", "2022-03-11", DB)

    # sort the rankings according to the new ratings
    ranks = DB.sortRankings(ranks)

    # Update the player objects with their new rankings
    DB.updatePlayerRankings(ranks)

    # output the updated player data to the data files
    for player in ranks.values():
        playerLoader.savePlayer(directory, player)

    print("Completed processing 2022 Campbell River tournament.\n\n")

    # Victoria Closed
    matchfile = "Tournaments/2022/2022_VictoriaClosed.csv"

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
            dest.write("\n")

    DB.numberPlayers = len(ranks)

    # Process the matches and update the ratings
    ranks = matches.processMatches(ranks, matchfile, matchlist, "2022 Victoria Closed", "2022-05-06", DB)

    # sort the rankings according to the new ratings
    ranks = DB.sortRankings(ranks)

    # Update the player objects with their new rankings
    DB.updatePlayerRankings(ranks)

    # output the updated player data to the data files
    for player in ranks.values():
        playerLoader.savePlayer(directory, player)

    print("Completed processing 2022 Victoria Closed tournament.\n\n")



    # Provincial Championships
    matchfile = "Tournaments/2022/2022_Provincials.csv"

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
            dest.write("\n")

    DB.numberPlayers = len(ranks)

    # Process the matches and update the ratings
    ranks = matches.processMatches(ranks, matchfile, matchlist, "2022 Provincial Championships", "2022-05-27", DB)

    # sort the rankings according to the new ratings
    ranks = DB.sortRankings(ranks)

    # Update the player objects with their new rankings
    DB.updatePlayerRankings(ranks)

    # output the updated player data to the data files
    for player in ranks.values():
        playerLoader.savePlayer(directory, player)

    print("Completed processing 2022 Provincials.\n\n")


    # New Era Open
    matchfile = "Tournaments/2022/2022_NewEra.csv"

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
            dest.write("\n")

    DB.numberPlayers = len(ranks)

    # Process the matches and update the ratings
    ranks = matches.processMatches(ranks, matchfile, matchlist, "2022 New Era Open", "2022-08-05", DB)

    # sort the rankings according to the new ratings
    ranks = DB.sortRankings(ranks)

    # Update the player objects with their new rankings
    DB.updatePlayerRankings(ranks)

    # output the updated player data to the data files
    for player in ranks.values():
        playerLoader.savePlayer(directory, player)

    print("Completed processing 2022 New Era Open.\n\n")



    # Nanaimo Open
    matchfile = "Tournaments/2022/2022_NanaimoOpen.csv"

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
            dest.write("\n")

    DB.numberPlayers = len(ranks)

    # Process the matches and update the ratings
    ranks = matches.processMatches(ranks, matchfile, matchlist, "2022 Nanaimo Open", "2022-10-08", DB)

    # sort the rankings according to the new ratings
    ranks = DB.sortRankings(ranks)

    # Update the player objects with their new rankings
    DB.updatePlayerRankings(ranks)

    # output the updated player data to the data files
    for player in ranks.values():
        playerLoader.savePlayer(directory, player)

    print("Completed processing 2022 Nanaimo Open.\n\n")



    # Thanksgiving Tournament
    matchfile = "Tournaments/2022/2022_Thanksgiving.csv"

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
            dest.write("\n")

    DB.numberPlayers = len(ranks)

    # Process the matches and update the ratings
    ranks = matches.processMatches(ranks, matchfile, matchlist, "2022 C1 Thanksgiving Tournament", "2022-10-08", DB)

    # sort the rankings according to the new ratings
    ranks = DB.sortRankings(ranks)

    # Update the player objects with their new rankings
    DB.updatePlayerRankings(ranks)

    # output the updated player data to the data files
    for player in ranks.values():
        playerLoader.savePlayer(directory, player)

    print("Completed processing 2022 Thanksgiving Tournament.\n\n")



    # Island Open
    matchfile = "Tournaments/2022/2022_IslandOpen.csv"

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
            dest.write("\n")

    DB.numberPlayers = len(ranks)

    # Process the matches and update the ratings
    ranks = matches.processMatches(ranks, matchfile, matchlist, "2022 Island Open", "2022-11-19", DB)

    # sort the rankings according to the new ratings
    ranks = DB.sortRankings(ranks)

    # Update the player objects with their new rankings
    DB.updatePlayerRankings(ranks)

    # output the updated player data to the data files
    for player in ranks.values():
        playerLoader.savePlayer(directory, player)

    print("Completed processing 2022 Islands.\n\n")
 
    
    # END OF YEAR UPDATES

    print("Tournament match processing complete!")

    # Update rankings(?) and highestRank
    for p in ranks.values():
        if(p.highestRank == "NR"):
            p.highestRank = p.rank
        elif(p.rank != "NR"):
            if int(p.rank) > int(p.highestRank):
                p.highestRank = p.rank

    # Print  final rankings
    print("Total number matches processed:", DB.matchesPlayed)
    print("Total number players ranked:", DB.numberPlayers)
    print("Final 2022 Rankings:")
    DB.outputRankingsToConsole(ranks)
    DB.outputRankingsToCSV(ranks, savestate)

    # Update previousAnnualRatings (do after printing, so you print the old previous annual rankings and then set them to the current ones.)
    for p in ranks.values():
        # Update the variables
        p.previousAnnualRank = p.rank
        p.previousAnnualRating = p.rating
        # Save them to the file!
        playerLoader.savePlayer(directory, p)

    # Save progress in tdata
    DB.save()
    print(f"Final rankings have been saved to {savestate}.\n")

    
    return

PROCESS_2022_TOURNAMENTS()