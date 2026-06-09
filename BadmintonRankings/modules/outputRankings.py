import csv
from modules import player

# Sort the rankings
def sortRankings(ranks):
    ranks = dict(sorted(ranks.items(), key=lambda item: item[1].rating, reverse=True))
    return ranks

# Update rankings in player objects
def updatePlayerRankings(ranks):
    rank = 1
    for player in ranks.values():
        player.previousAnnualRank = player.rank
        player.rank = rank
        rank += 1
        if rank < player.highestRank:
            player.highestRank = player.rank
            player.matchHistory.append(f"New highest rank achieved: {player.highestRank}")
    return

def updatePreviousAnnualRatings(ranks):
    for p in ranks:
        ranks[p].previousAnnualRating = int(ranks[p].rating)
        print("Updating Previous Annual Rankings!")
    return ranks

# Print to console
def outputRankingsToConsole(ranks):
    for player in ranks.values():
        print(f"Rank:{player.rank}\tRating:{player.rating}\t{player.name}\tW-L:{player.wins}-{player.losses}\tRating+/-:{player.rating - player.previousAnnualRating}\tRank+/-:{player.rank - player.previousAnnualRank}")
    return

def outputRankingsToCSV(ranks, outputFile):
    with open(outputFile, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        for player in ranks.values():
            csv_writer.writerow([player.rating, player.name, player.id, player.wins, player.losses, player.rank, player.rating-player.previousAnnualRating])
    print(f"Rankings have been output to {outputFile}")
    return