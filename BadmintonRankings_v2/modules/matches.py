import csv
from modules import player as player
from modules import saveSystem as saveSystem

# Process the matches and return the rankings
def processMatches(ranks, tournamentFile, matchlist,tournamentName, tournamentDate, save):
    with open(tournamentFile, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            # Set variables for winner and loser ( for readability )
            WP = ranks[row[2]]
            LP = ranks[row[4]]
            # Initialize separate K values for winner and loser
            # K values are calculated based on the number of wins and losses so that new players have more sensitive ratings
            WK = WP.update_confidence()
            LK = LP.update_confidence()
            # Determine Rating for winning (A) player
            RA = WP.rating
            # Determine rating for losing (B) player
            RB = LP.rating
            # Determine expected outcome for winning player using formula 1
            EA = 1 / ( 1+pow(10,(RB-RA)/400))
            # Determine expected outcome for losing player using formula 1
            EB = 1 / ( 1+pow(10,(RA-RB)/400))
            # Determine true outcome for both players
            SA = 1
            SB = 0
            # Update the ratings according to formula 2
            WP.rating = int(RA + WK*(SA-EA))
            LP.rating = int(RB + LK*(SB-EB))
            # Update wins and losses
            WP.wins += 1
            LP.losses += 1

            WP.matchHistory.append(f"Defeated {LP.name} in {row[0]} of {tournamentName}: +{WP.rating - RA} points for a new rating of {WP.rating}")
            LP.matchHistory.append(f"Lost to {WP.name} in {row[0]} of {tournamentName}: {(LP.rating - RB)} points for a new rating of {LP.rating}")

            # Update titles if applicable
            if row[0] == 'Finals' or row[0] == 'Final' or row[0] == 'A Finals':
                WP.titles.append(f"{tournamentName} Champion")
                LP.titles.append(f"{tournamentName} Runner-up")
                save.winners.append([tournamentName, tournamentDate, WP.name, WP.id])

            if WP.rating > WP.highestRating:
                WP.highestRating = WP.rating
                WP.matchHistory.append(f"New highest rating achieved: {WP.highestRating}")

            save.matchesPlayed += 1

            print(f"Processed {row[0]} match: {WP.name} defeats {LP.name}")
            print(f"{WP.name} +{WP.rating - RA} New rating: {WP.rating}")
            print(f"{LP.name} {LP.rating - RB} New rating: {LP.rating}")
    return ranks