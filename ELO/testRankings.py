import csv

input_filename = 'inputRankings.csv'
ranks = {}

# Load data from inputRankings.csv into the ranks dictionary
with open(input_filename, newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        player_name = row[0]
        rating = int(row[1])
        ranks[player_name] = rating

print(ranks)