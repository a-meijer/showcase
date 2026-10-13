import csv

INPUT_FILE = "data/output.csv"

headers = [
    "Rank",
    "Rating",
    "Name",
    "ID",
    "Wins",
    "Losses",
    "Previous Rank",
    "Previous Rating",
    "Latest Tournament",
]

with open(INPUT_FILE, newline="", encoding="utf-8") as f:
    rows = list(csv.reader(f))

print("|" + "|".join(headers) + "|")
print("|" + "|".join(["---"] * len(headers)) + "|")

for row in rows:
    rating, rank, name, pid, wins, losses, prev_rank, prev_rating, latest_tournament = row

    print(
        f"|{rank}|{rating}|{name}|{pid}|{wins}|{losses}|{prev_rank}|{prev_rating}|{latest_tournament}|"
    )