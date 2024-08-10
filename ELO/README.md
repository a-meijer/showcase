## ReadMe
### Purpose
To demonstrate a ranking system for badminton that is more accurate than the official rankings for British Columbia.

### Introduction
As of August 2024, the official Badminton BC Senior Men's Singles Rankings are based on tournament results (placement) in only two tournaments, posted on May 14, 2024:
 - 2024 Jack Underhill
 - 2024 Provincial Championships

https://badmintoncanada.tournamentsoftware.com/ranking/category.aspx?id=39968&category=415

A ranking based on tournament placement alone is suboptimal because the luck of the draw creates inaccuracies in the rankings compared to what can be achieved with a ranking system based on match results, especially because tournament organizers use a Single Elimination format instead of Double Elimination. Double Elimination creates a more accurate placement result, a higher-resolution result (if you will). Plus, it makes the matches more meaningful because it doesn't require any consolation matches. Copying match data from tournaments on badmintoncanada.tournamentsoftware.com and creating a ranking system based on match results is another way to create a higher resolution ranking, especially with a large number of matches. The more data, the better.
The Elo Ranking System can be used with CSV files to easily create ranking systems for almost any competitive activity. 

The algorithm for this project is written in Python and the data is stored in CSV files.

### Creating CSV Files With Match Data
The first iteration of prototypes for this ELO ranking system run on only the data from the same tournaments that contribute to the 2024 rankings. This is to demonstrate how changes to the algorithm's initialization affect the results. Later iterations will include match results from additional tournaments.
Matches are publicly available on badmintoncanada.tournamentsoftware.com, but apparently it is against the site policy to use automation to scrape the website for data. It is easy enough to manually copy and paste the match results into spreadsheets.

Here is the link to the Men's Singles draw match page for the 2024 Jack Underhill:

https://badmintoncanada.tournamentsoftware.com/sport/drawmatches.aspx?id=6DBC438D-5F21-4544-9A89-C651CE550C1B&draw=11

Here is the link to the Men's Singles draw match page for the 2024 Provincial Championships:

https://badmintoncanada.tournamentsoftware.com/sport/drawmatches.aspx?id=5F17FF22-3C9F-4199-AE91-C0838750A59E&draw=22

After getting the match data ready for the initial prototypes, I ran a test program to create a CSV containing the rankings and I confirmed there were no duplicates. Notably, when adding more tournaments, it becomes important to ensure no player has duplicate entries in the rankings.

### Understanding the Algorithm
#### Elo's Formulas
Arpad Elo was nice enough to publish the formulas for his ELO algorithm, and they are now available on Wikipedia. His algorithm requires two formulas. https://en.wikipedia.org/wiki/Elo_rating_system

#### Formula 1:
![FormulaImage](formula1.jpg)

``
EA = 1/(1 + 10^((RB-RA)/400))
``

#### Formula 2:
![FormulaImage](formula2.jpg)

``
R'A = RA + K(SA - EA)
``

To implement the algorithm intelligently, it's important to understand what these formulas do and what the variables are for.

``

    EA = Expected outcome for player A in A v.s. B

    RA = Rating of player A

    RB = Rating for player B

    R'A = Updated Rating for player A

    K = Sensitivity constant

    SA = Outcome for player A
``

#### Using the Formulas Algorithmically
The operators and data structures in Python make implementing this formula a breeze.
I decided to create Player objects and point to them in a Python dictionary, indexed by player name. If two players have a match together, the algorithm selects their ratings from the rank dictionary, loads in the match result to the S variable, selects a K constant (if necessary), and then runs the formulas! Formula 1 calculates the expected outcome (between 0 and 1) for each player and Formula 2 updates the rankings.
 - After the tournament, process each match in chronological order
 - For each match, load the current ratings for the two players in the match
 - Load the match result into the S variable (for the formulas)
 - Set a K value for the formula
 - Run Formula 1 to calculate the expected outcome
 - Run Formula 2 to update the ratings according to the match result (true outcome) and expected outcome from Formula 1
Repeat for each match in the dataset, and then output the new rankings when done.

#### Considering an Object Oriented Solution
Creating Player objects is something I went back and forth on during the development of this project. It would've been possible to do the algorithm with just a list of tuples. In the end I decided to go with Player objects because they are conceptually easy to work with and they're easily scaleable in case I want to add more features like match history and player aliases.

### Initial Prototype No.1: updateRankings.py
The name of the file to run on the CSV data is called updateRankings.py.
Use the following command:
``
python updateRankings.py
``
ChatGPT greatly enhanced my productivity for this project by helping to answer questions about Python syntax. I created my Python file in VSCode and implemented the Elo algorithm.

The file runs from top to bottom of course, it imports the CSV library; declares filename variables; initializes the Player class, the rank dictionary, and the K-constant, all global variables; and creates a function that I later use to sort the rankings.

Once inside the body of the Python code, it opens the rankings CSV file. Now, I already have my CSV file pre-made, but if you need to make your own, as I may have mentioned earlier, it's a simple Python procedure of outputting a Set of names from the match CSV to a different CSV file. The rankings are loaded in as a Python dictionary indexed by player names, pointing to Player objects. I open the match data file and include the crux of the algorithm:

``

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
        
        # Update the ratings according to formula 2   
        ranks[row[0]].rating = int(RA + K*(SA-EA))   
        ranks[row[1]].rating = int(RB + K*(SB-EB))
        
``

With that out of the way and the files closed, I sort the ratings and then print them to console and file. If you do this, make sure to name your output file differently than your input files so you don't overwrite anything important.

#### Tuning the Algorithm
The initial prototype works according to the code snippet above and there are a few ways to change it meaningfully such as by choosing a different K-value or adapting the initial rankings, without reimplementing the entire algorithm. This will be demonstrated later in Variations.

#### Choosing The K-Value for Rating Sensitivity
The K value is set as a constant 100 in the initial prototype and it affects the amount of rating change after a single match. The algorithm could be improved by using a dynamic K-value that changes based on the recent match results of each player. This is demonstated later in Variations.

#### Comparing the Initial Prototype to Initial Rankings
 - outputRankings1.csv is the ranking produced from the my initial prototype
 - officialRankings.csv is the rankings from Badminton BC based on Tournament Points
As expected, due to the extremely low number of matches for these ratings, consolation players get overrated and there are some unfortunate bad ratings, but with a few changes to the algorithm, this can be fixed. Besides, the accuracy would improve with more match data. Note that the BC Rankings are based on points from tournament placement where as the ELO Rankings are based on match results. This is a foundational difference, and proponents of a ranking based on tournament placement might argue that a ranking based on match results is artificial and would somehow spoil the competition, as if players don't achieve high tournament placement by winning matches (especially against strong opponents). Paradoxical though it may seem at first, this project later demonstrates that a ranking based on match results can more accurately represent (and predict) tournament placement than a ranking system based on placement alone.

What would improve the accuracy of this prototype the most is addressing the problem of consolation players being overranked. There are many ways to improve this algorithm. Consider the sample of possible variations below.

### Variations
 - Changing K value based on consolation
 - Changing K value based on streakiness/round/depth (this emphasizes the reduced K value in consolation Variation 1)
 - Using function of tournament points as initial ranking
 - Changing K value based on number of games in the match (if you go three games and get to extra points in the third, you don't lose as much ranking).
 - Combined Variation (combining all previous variations)
 - Changing K value based on the tournament type (see Badminton BC page for how that works on tournament points)
 - Reducing K value based on number of tournaments played

#### Prototype No.2 consolationFix.py: Lower K Value For Consolation
In the current tournament ruleset, if a player loses their first match in the Single Elimination bracket, they are eligible for Consolation bracket, so that every player can play two matches. The problem of consolation matches would be solved automatically by switching to a Double Elimination format, but as it is, this problem can be solved by first separating each tournament into its own CSV file. Secondly, a Consolation champion shouldn't gain as much ranking as a player who wins their first round match, so divide default constant K value by the number of Consolation rounds or by 4 to get a simple approximation. For a bracket of 16 players, there are 3 rounds; for a bracket of 32 players, there are 4 rounds; for a bracket of 64 players, there are 5 rounds, and so on.
 - 2024Tournament_JackUnderhill.csv
 - 2024Tournament_Provincials.csv

#### Prototype No.3 winningStreaks.py: Higher K Value For Winning Streaks
Now that we have a K value that changes based on the match results for each player, this can be applied to the Main Draw of the Single Elimination Bracket as well as Consolation. Getting deep into a tournament bracket should empower players to win more ELO points, and this contrasts with the lower K value in Consolation.

#### Prototype No.4 pointsVariation.py: Tournament Points As Initial Ranking
So far, all of the variations have started with each player rated at 1000 ELO rating points. Why not initialize the players with an average of 1000 and their tournament points from the official rankings? It is an intuitive place to start, to get a rough idea of the player levels.

#### Prototype No.5 matchDetailVariation.py: Going Three Games
If you lose in three games in a ranked match and get to extra points in the third game, lose half as much rating because it is such a close match.

#### Prototype No.6 combinedVariation.py: Combining All Four Above Variations
Work in progress

#### Prototype No.7 advancedVariation.py: Tournament Type, Tournaments Played, and High Ratings
Work in progress

### Variations Compared to Official Rankings
Work in progress

### Conclusion
Work in progress

### Author
Andrew Meijer
andrew@atrm.ca
