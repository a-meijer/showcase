# VARIATION 1 IS FOR CONSOLATION K VALUE ADJUSTMENT
# Matches in consolation aren't as important for rating, so REDUCE the K value.
# Considering the Single Elimination format, a consolation champion should not have significantly more rating gain than a player who reaches the second round of the main draw.
# Therefore, since there are usually 3 to 5 rounds in consolation depending if the draw has 16, 32, or 64 entrants, this program divides the K-value by 4 for all consolation matches.
# A match is determined to be consolation when the players have already lost a match in the event being processed.
# Each event will need to be broken into a different file and processed one at a time.

import csv

# Run the program for each tournament and manually update the inputs for each run
input_matches_filename = '2024Tournament_Provincials.csv'
input_rankings_filename = 'outputVariation1.csv'
output_filename = 'outputVariation1.csv'

class Player:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating
        self.consolation = False

# Initialize ranks dictionary
ranks = {}

# Set K constant
K = 100

# Pass this function to the sorting algorithm
# sort_by_rating is used by the sorting algorithm
def sort_by_rating(player):
    return player.rating

# Load data from inputRankings.csv into the ranks dictionary
with open(input_rankings_filename, newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        player_name = row[0]
        rating = int(row[1])
        ranks[player_name] = Player(player_name, rating)

# Open the match data file
with open(input_matches_filename, newline='') as csvfile:
    # Create a CSV reader object
    csv_reader = csv.reader(csvfile)
    
    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Determine Rating for winning player
        RA = ranks[row[0]].rating
        # Determine rating for losing player
        RB = ranks[row[1]].rating
        # Determine expected outcome for winning player using formula 1
        EA = 1 / ( 1+pow(10,(RB-RA)/400))
        # Determine expected outcome for losing player using formula 1
        EB = 1 / ( 1+pow(10,(RA-RB)/400))
        # Determine true outcome for both players
        SA = 1
        SB = 0
        # Set the K value in a temporary variable
        tK = K
        # Change the K value if consolation==True
        if(ranks[row[0]].consolation):
            tK = tK/4
        
        # Update the ratings according to formula 2
        ranks[row[0]].rating = int(RA + tK*(SA-EA))
        ranks[row[1]].rating = int(RB + tK*(SB-EB))
        # Update consolation boolean for losing player
        ranks[row[1]].consolation = True

# Sort by rating
sorted_players = sorted(ranks.values(), key=sort_by_rating, reverse=True)
ranks = {player.name: player for player in sorted_players}

# Print all ratings   
for player_name, player_obj in ranks.items():
    print(f"{player_name}: {player_obj.rating}")       

# Open/Create the rankings output file  
with open(output_filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for player_name, player_obj in ranks.items():
        writer.writerow([player_name, player_obj.rating])