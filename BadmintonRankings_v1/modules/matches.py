import csv
from modules import player

# Process the matches and return the rankings
def processMatches(ranks, K, tournamentFile, tournamentName):
    numMatchesProcessed = 0
    with open(tournamentFile, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            # Initialize separate K values for winner and loser
            # K values are calculated based on the number of wins and losses so that new players have more sensitive ratings
            WK = int(K*(ranks[row[2]].wins + ranks[row[2]].losses + 2)/(ranks[row[2]].wins + ranks[row[2]].losses + 1))
            LK = int(K*(ranks[row[4]].wins + ranks[row[4]].losses + 2)/(ranks[row[4]].wins + ranks[row[4]].losses + 1))
            # Determine Rating for winning (A) player
            RA = ranks[row[2]].rating
            # Determine rating for losing (B) player
            RB = ranks[row[4]].rating
            # Determine expected outcome for winning player using formula 1
            EA = 1 / ( 1+pow(10,(RB-RA)/400))
            # Determine expected outcome for losing player using formula 1
            EB = 1 / ( 1+pow(10,(RA-RB)/400))
            # Determine true outcome for both players
            SA = 1
            SB = 0
            # Update the ratings according to formula 2
            ranks[row[2]].rating = int(RA + WK*(SA-EA))
            ranks[row[4]].rating = int(RB + LK*(SB-EB))
            # Update wins and losses
            ranks[row[2]].wins += 1
            ranks[row[4]].losses += 1
            # Update titles if applicable
            # if row[0] == 'Finals':
              #   ranks[row[2]].titles.append(f"{tournamentName} Champion")
              #   ranks[row[4]].titles.append(f"{tournamentName} Finalist")

            print(f"Processed {row[0]} match: {ranks[row[2]].name} defeats {ranks[row[4]].name}")
            print(f"{ranks[row[2]].name} +{ranks[row[2]].rating - RA} New rating: {ranks[row[2]].rating}")
            print(f"{ranks[row[4]].name} {ranks[row[4]].rating - RB} New rating: {ranks[row[4]].rating}")
    return ranks