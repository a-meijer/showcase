import csv

# Hard-coded input selection; get with the program.
input_matches_filename = '2024Tournament_Provincials.csv'
input_rankings_filename = 'officialRankings.csv'
output_filename = 'sourceRankings.csv'

class Player:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

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
        rating = int((int(row[1])+1000)/2)
        ranks[player_name] = Player(player_name, rating)

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