import csv
from modules import player as player
from modules import saveSystem as saveSystem
from datetime import date

# Process the matches and return the rankings
def processMatches(ranks, tournamentFile, tournamentName, tournamentDate, save):
    # Set constants
    BASE_K = 100 # Base maximum rating change per match
    INITIAL_RD = 300 # Initial rating rating point uncertainty
    MIN_RD = 50 # Minimum rating point uncertainty
    MAX_RD = 350 # Maximum rating point uncertainty
    RD_INCR = 10 # Uncertainty decrease per match played
    RD_INAC = 5 # Uncertainty increase per month of inactivity

    with open(tournamentFile, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:

            # Set variables for winner and loser ( for readability )
            WP = ranks[row[2]]
            LP = ranks[row[4]]

            # Determine the RD increase based on the number of days since the last match for both players
            Wdays = 0 # Number of days since winner's last match
            Ldays = 0 # Number of days since loser's last match
            if WP.latestTournament:
                Wdays = (date.fromisoformat(tournamentDate) - date.fromisoformat(WP.latestTournament)).days
            if LP.latestTournament:
                Ldays = (date.fromisoformat(tournamentDate) - date.fromisoformat(LP.latestTournament)).days
            WP.RD += int(Wdays / 30 * RD_INAC)
            WP.RD = min(MAX_RD, WP.RD)
            LP.RD += int(Ldays / 30 * RD_INAC)
            LP.RD = min(MAX_RD, LP.RD)

            # Use the "Glicko" algorithm to determine the K values based on the RDs for both players
            WK = WP.glick(LP, BASE_K, INITIAL_RD) # BASE_K and INITIAL_RD
            LK = LP.glick(WP, BASE_K, INITIAL_RD)

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

            # Update the Rating Deviation variables for the match being played
            WP.RD -= RD_INCR
            LP.RD -= RD_INCR
            WP.RD = max(MIN_RD, WP.RD)
            LP.RD = max(MIN_RD, LP.RD)

            WP.matchHistory.append(f"Defeated {LP.name} in {row[0]} of {tournamentName}: +{WP.rating - RA} points for a new rating of {WP.rating}")
            LP.matchHistory.append(f"Lost to {WP.name} in {row[0]} of {tournamentName}: {(LP.rating - RB)} points for a new rating of {LP.rating}")

            # Update latestTournament for both players
            WP.latestTournament = tournamentDate
            LP.latestTournament = tournamentDate

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