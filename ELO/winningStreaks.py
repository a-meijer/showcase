import csv

# Hard-coded input selection; get with the program.
input_matches_filename = '2024Tournament_Provincials.csv'
input_rankings_filename = 'outputRankingsV3.csv'
output_filename = 'outputVariation2.csv'

class Player:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating
        self.winningStreak = 0

# Initialize ranks dictionary
ranks = {}

# Set K constant
K = 100

# Pass this function to the sorting algorithm
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
        # Set a different K value for the winner, incorporating winningStreak (see readme)
        KW = K + (ranks[row[0]].winningStreak)*(K/4)
        # Update the ratings according to Formula 2
        ranks[row[0]].rating = int(RA + KW*(SA-EA))
        ranks[row[1]].rating = int(RB + K*(SB-EB))
        # Update the winning streaks
        ranks[row[0]].winningStreak += 1
        ranks[row[1]].winningStreak = 0

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