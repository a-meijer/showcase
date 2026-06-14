import csv

with open("data/output.csv", newline="", encoding="utf-8") as f:
    rows = list(csv.reader(f))

headers = ["Rank", "Rating", "Name", "ID", "Wins", "Losses"]

print("|" + "|".join(headers) + "|")
print("|" + "|".join(["---"] * len(headers)) + "|")

for row in rows:
    rating, name, pid, wins, losses, rank, _ = row
    print(f"|{rank}|{rating}|{name}|{pid}|{wins}|{losses}|")