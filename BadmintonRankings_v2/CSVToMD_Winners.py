import csv
from datetime import datetime

INPUT_FILE = "data/tdata.csv"

headers = [
    "Start Date",
    "Name",
    "Champion",
]

with open(INPUT_FILE, newline="", encoding="utf-8") as f:
    rows = list(csv.reader(f))

print("|" + "|".join(headers) + "|")
print("|" + "|".join(["---"] * len(headers)) + "|")

# Skip the first row (metadata)
for tournament_name, start_date, champion, _ in rows[1:]:

    date = datetime.strptime(start_date, "%Y-%m-%d")
    formatted_date = date.strftime("%b %d, %Y").replace(" 0", " ")

    print(f"|{formatted_date}|{tournament_name}|{champion}|")