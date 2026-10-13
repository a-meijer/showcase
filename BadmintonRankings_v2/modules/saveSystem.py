import csv
from modules import player
from datetime import datetime

class SaveSystem:
    def __init__(self, matchlist, savestate, tdata):
        self.matchlist = matchlist      # not in use
        self.savestate = savestate      # not in use
        self.tdata = tdata              # tdata filename
        self.matchesPlayed = 0          # total number of matches played all time
        self.numberPlayers = 0          # total number of players all time
        self.winners = []               # list of [tournament name, date, player name, ID]
        self.totalRP = 0                # total rating points in the system after match processing
        self.mostWins = 0               # Keep track of most wins in def trackWins
        self.mostMatches = 0            # Keep track of most matches in def trackMatches
        self.MostActivePlayer = None    # Player ID with the most matches played all time
        self.MostWinsPlayer = None      # Player ID with the most match wins of all time

    # Add to Total RP
    def addRP(self, num):
        self.totalRP += num

    # Track most winning player
    def trackWins(self, player):
        if(player.wins > self.mostWins):
            self.mostWins = player.wins
            self.MostWinsPlayer = player.id

    # Track most active player
    def trackMatches(self, player):
        totalMatches = player.wins + player.losses
        if(totalMatches > self.mostMatches):
            self.mostMatches = totalMatches
            self.MostActivePlayer = player.id

    # Write data out to tdata
    def save(self):
        with open(self.tdata, 'w', newline='') as file:
            csv_writer = csv.writer(file)
            # Write all the variables on the first row
            csv_writer.writerow([self.matchesPlayed, self.numberPlayers, self.totalRP, self.MostWinsPlayer, self.mostWins, self.MostActivePlayer, self.mostMatches])
            # Write all the tournament winners, each on their own rown
            for r in self.winners:
                csv_writer.writerow(r)
        return

    # Read data in from tdata
    def load(self):
        with open(self.tdata, 'r') as file:
            firstRow = True
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if(firstRow):
                    firstRow = False
                    self.matchesPlayed = int(row[0])
                    self.numberPlayers = int(row[1])
                    self.MostWinsPlayer = row[3]
                    self.mostWins = int(row[4])
                    self.MostActivePlayer = row[5]
                    self.mostMatches = int(row[6])

                else:
                    self.winners.append(row)
        return

    #METHODS MIGRATED FROM OLD outputRankings.csv
    # Sort the rankings
    def sortRankings(self, ranks):
        ranks = dict(sorted(ranks.items(), key=lambda item: item[1].rating, reverse=True))
        return ranks

    # Update rankings in player objects
    # New changes for rank polishing, October 2026
    # The way I have it now, this runs after every tournament!
    def updatePlayerRankings(self, ranks, tdate):
        rank = 1
        # Loop for each player from highest rating to lowest
        for player in ranks.values():

            # Players get a ranking iff
            # 1. they have won a match
            # 2. they played a tournament in the last 365 days.

            latestTourney = datetime.strptime(tdate, "%Y-%m-%d").date()
            activeTourney = datetime.strptime(player.latestTournament, "%Y-%m-%d").date()
            daysSinceLastTournament = (latestTourney - activeTourney).days

            if daysSinceLastTournament > 365:
                player.rank = "NR"
                continue

            if player.wins <= 0:
                player.rank = "NR"
                continue

            player.rank = rank
            rank += 1
            if player.highestRank == "NR":
                player.highestRank = player.rank
            elif rank < int(player.highestRank):
                player.highestRank = player.rank
                player.matchHistory.append(f"New highest rank achieved: {player.highestRank}")

            continue   

        return

    # Print to console
    def outputRankingsToConsole(self, ranks):
        for player in ranks.values():
            print(f"Rank:{player.rank}\tRating:{player.rating}\t{player.name}\tW-L:{player.wins}-{player.losses}\tWinrate:{player.winrate()}\tRating+/-:{player.rating - player.previousAnnualRating}\tPrevious Rank:{player.previousAnnualRank}")
        return

    # Output to CSV
    def outputRankingsToCSV(self, ranks, outputFile):
        with open(outputFile, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            for player in ranks.values():
                csv_writer.writerow([player.rating, player.rank, player.name, player.id, player.wins, player.losses, player.previousAnnualRank, player.previousAnnualRating, player.latestTournament])
        print(f"Rankings have been output to {outputFile}")
        return