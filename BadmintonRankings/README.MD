## ReadMe
### Purpose
The purpose of this project is to maintain a Provincial rating system for Men's Singles badminton players based on the official ranking system for British Columbia, using the tournaments that award points towards the official rankings.

### Introduction
For more information on how the ELO rating system works, see the initial prototype: [github.com/a-meijer/showcase](https://github.com/a-meijer/showcase/tree/master/ELO)
For more information on the ongoing development process, see devlog.txt.
Match data is available on Google Drive:
https://drive.google.com/drive/folders/1GX5JPSUZaMUrkilviBPgyZCzfP7bpef-?usp=sharing

The match data for each tournament is in CSV files in the tournaments directory.

### The Validity And Accuracy of the Ratings
The theory behind what makes this rating system more accurate than the official rankings is that it depends on match results rather than tournament placement.
The results of individual matches affect rating points, not the results of tournaments. For example, if you lost in the first round of a tournament to a high rank opponent, that wouldn't affect your rating as much as losing to a low rank oppoent.
To reconcile these ratings with the official provincial rankings, I will only use the results from tournaments that affect the official rankings.

### The First Tournament
There were no provincial ranking tournaments in 2020 or 2021, and since tournaments only affect the official rankings for two years, the official rankings were reset in 2022.
Therefore, it is fitting to start this ratings project from the first provincial ranking tournament in 2022, when the provincial rankings were reset. 
The Provincial Ratings will be aligned with the official rankings in this way.
As new tournament results are incorporated into the official rankings, they will also be incorporated into these ratings according to the purpose of this project.

### About The Initial Prototype
The initial prototype for this project is called "ELO": [github.com/a-meijer/showcase](https://github.com/a-meijer/showcase/tree/master/ELO)
At the time of the initial prototype, in the Summer of 2024, it was easy to copy and past the match results from each tournament into spreadsheets to use for the ELO ratings algorithm.
Unfortunately, due to a reformatting of the website, it is no longer as easy to copy the match data from the match pages. Henceforth I will manually copy the match data into spreadsheets.
The silver lining of this is that manually copying the match data into spreadsheets makes it is easier to avoid copying the consolation matches which should not affect rating points.

### How To Use The Rating System
To use the rating algorithm, run the program: src/main.py
By default, the program selects "Ratings.csv" as the input data file, but you may opt for a different filename.
The program selects "RatingsOutput.csv" as the default output data file, but you may change the filename; just be careful not to overwrite anything.
You will need to enter the filename for the tournament match data you are processing. You will need to approve the initial rankings for new players.
Now RankingsOutput.csv should be used as the input data file for the next tournament.
You can run printRankings.py RankingsOutput.csv to display the new rankings.

### Ratings


### Tournaments
2022 BC OPEN AND U-23 PROVINCIAL CHAMPIONSHIP
2023 Jack Underhill Open
2023 BC Junior A, U23 and Open Provincial Championship
2024 VRC Jack Underhill Open A and B Tournament
2024 BC Junior A and Open Provincial Championship (U15,U17,U23, Open A & B)
Wing’s Open Badminton Tournament
Shuttlesport Open Series #2
2025 VRC Jack Underhill Open A & B Tournament
2025 BC Junior A, Open A and Open B Provincial Championships

### Author
Andrew Meijer