# Hardcode everything to bypass user input and test on all tournament data at once

import os
from modules import io as myio
from modules import loadPlayers as playerLoader
from modules import saveSystem as saveSystem
from modules import matches as matches
from modules import player as player
from modules import saveSystem as saveSystem


def run(matchlist, savestate, tdata, directory, matchfiles, tnames, tdates, yname):

    # Initialize ranks dictionary
    ranks = {}

    # Create savestate object
    DB = saveSystem.SaveSystem(matchlist, savestate, tdata)

    # Load the saved data
    DB.load()

    # Load extant players into ranks, the list of players
    ranks = playerLoader.loadPlayers(ranks, directory)

    for matchfile, tname, tdate in zip(matchfiles,tnames,tdates):

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
        ranks = matches.processMatches(ranks, matchfile, tname, tdate, DB)

        # sort the rankings according to the new ratings
        ranks = DB.sortRankings(ranks)

        # Update the player objects with their new rankings
        DB.updatePlayerRankings(ranks, tdate)

        # output the updated player data to the data files
        for player in ranks.values():
            playerLoader.savePlayer(directory, player)

        print("Finished processing",tname,"\n")


    # END OF YEAR UPDATES

    print("Tournament match processing complete!")

    # Update highestRanks
    for p in ranks.values():
        if(p.highestRank == "NR"):
            p.highestRank = p.rank
        elif(p.rank != "NR"):
            if int(p.rank) > int(p.highestRank):
                p.highestRank = p.rank

    # Print  final rankings
    print("Total number matches processed:", DB.matchesPlayed)
    print("Total number players ranked:", DB.numberPlayers)
    # print(f"Final {yname} Rankings:")
    # DB.outputRankingsToConsole(ranks)
    DB.outputRankingsToCSV(ranks, savestate)

    # For each player. . .
    for p in ranks.values():
        # add player rating to the sum of ratings
        DB.addRP(p.rating)
        # find the most winning player
        DB.trackWins(p)
        # find the player with most matches played
        DB.trackMatches(p)
        # Update previousAnnualRatings
        p.previousAnnualRank = p.rank
        p.previousAnnualRating = p.rating
        playerLoader.savePlayer(directory, p)

    # Save progress (to tdata)
    DB.save()

    return