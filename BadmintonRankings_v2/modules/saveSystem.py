import csv
from modules import player

class SaveSystem:
    def __init__(self, matchlist, savestate, tdata):
        self.matchlist = matchlist
        self.savestate = savestate
        self.tdata = tdata
        self.winners = []
        self.matchesPlayed = 0
        self.numberPlayers = 0
        self.winners = []

    def save(self):
        with open(self.tdata, 'w', newline='') as file:
            csv_writer = csv.writer(file) 
            csv_writer.writerow([self.matchesPlayed, self.numberPlayers])
            for r in self.winners:
                csv_writer.writerow(r)
        return
    
    def load(self):
        with open(self.tdata, 'r') as file:
            firstRow = True
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if(firstRow):
                    firstRow = False
                    self.matchesPlayed = int(row[0])
                    self.numberPlayers = int(row[1])
                else:
                    self.winners.append(row)
        return

    #METHODS MIGRATED FROM OLD outputRankings.csv
    # Sort the rankings
    def sortRankings(self, ranks):
        ranks = dict(sorted(ranks.items(), key=lambda item: item[1].rating, reverse=True))
        return ranks

    # Update rankings in player objects
    def updatePlayerRankings(self, ranks):
        rank = 1
        for player in ranks.values():
            if player.rank == "NR" and player.wins > 0:
                player.rank = rank
                player.highestRank = rank
                rank += 1
                player.matchHistory.append(f"First ranking achieved! Rank: {player.highestRank}")
            elif player.rank != "NR":    
                player.rank = rank
                rank += 1
                if player.highestRank == "NR":
                    player.highestRank = player.rank
                elif rank < int(player.highestRank):
                    player.highestRank = player.rank
                    player.matchHistory.append(f"New highest rank achieved: {player.highestRank}")
        return

    # Print to console
    def outputRankingsToConsole(self, ranks):
        for player in ranks.values():
            print(f"Rank:{player.rank}\tRating:{player.rating}\t{player.name}\tW-L:{player.wins}-{player.losses}\tWinrate:{player.winrate()}\tRating+/-:{player.rating - player.previousAnnualRating}\tPrevious Rank:{player.previousAnnualRank}")
        return

    def outputRankingsToCSV(self, ranks, outputFile):
        with open(outputFile, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            for player in ranks.values():
                csv_writer.writerow([player.rating, player.rank, player.name, player.id, player.wins, player.losses, player.previousAnnualRank, player.previousAnnualRating])
        print(f"Rankings have been output to {outputFile}")
        return