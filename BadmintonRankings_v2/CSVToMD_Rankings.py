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
]

with open(INPUT_FILE, newline="", encoding="utf-8") as f:
    rows = list(csv.reader(f))

print("|" + "|".join(headers) + "|")
print("|" + "|".join(["---"] * len(headers)) + "|")

for row in rows:
    rating, rank, name, pid, wins, losses, prev_rank, prev_rating = row

    print(
        f"|{rank}|{rating}|{name}|{pid}|{wins}|{losses}|{prev_rank}|{prev_rating}|"
    )