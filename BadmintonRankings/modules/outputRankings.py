import csv
from modules import player

# Sort the rankings
def sortRankings(ranks):
    ranks = dict(sorted(ranks.items(), key=lambda item: item[1].rating, reverse=True))
    return ranks

# Print to console
def outputRankingsToConsole(ranks):
    for player in ranks.values():
        print(f"{player.rating}\t{player.name}")
    return

def outputRankingsToCSV(ranks, outputFile):
    with open(outputFile, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        for player in ranks.values():
            csv_writer.writerow([player.rating, player.name, player.id, player.wins, player.losses])
    print(f"Rankings have been output to {outputFile}")
    return