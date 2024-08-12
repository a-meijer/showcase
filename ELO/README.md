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

    EA = Expected outcome for player A in A v.s. B

    RA = Rating of player A

    RB = Rating for player B

    R'A = Updated Rating for player A

    K = Sensitivity constant

    SA = Outcome for player A

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

|Rank|Official Rankings     |Tournament Points|Initial Prototype     |Rating|
|----|----------------------|-----------------|----------------------|------|
|1   |Saurabh Pandiar       |1488             |Saurabh Pandiar       |1352  |
|2   |Simar Singh           |935              |Nicholas Poon         |1192  |
|3   |Jalil Waiz            |930              |Simar Singh           |1176  |
|4   |Jack Chen             |810              |Lyem Fedoretz         |1164  |
|5   |Connor Nicholas Louie |805              |Victor Ho             |1116  |
|6   |Kwun Ho So            |685              |Jack Chen             |1116  |
|7   |Lyem Fedoretz         |533              |Ryan Liu              |1111  |
|8   |Uday Pratap Bharti    |520              |Jaden Thom            |1097  |
|9   |Sahil Rajesh Aggarwal |509              |Anish Chandra Jojula  |1087  |
|10  |Ratnesh Rao Ippili    |509              |Jalil Waiz            |1082  |
|11  |Victor Ho             |439              |Ayden Travis Lee      |1065  |
|12  |Ryan Liu              |439              |Connor Nicholas Louie |1050  |
|13  |Roy Hung              |400              |Shingchun (Kevin) Wu  |1043  |
|14  |Anish Chandra Jojula  |345              |Rickey Ruixi Zhang    |1042  |
|15  |Jaden Thom            |307              |Jasper Kong           |1036  |
|16  |Ayush Ayush           |307              |Uday Pratap Bharti    |1032  |
|17  |Rickey Ruixi Zhang    |225              |Yancong Li            |1032  |
|18  |Shingchun (Kevin) Wu  |225              |Ratnesh Rao Ippili    |1030  |
|19  |Jasper Kong           |225              |Stephen Dee           |1030  |
|20  |Stephen Dee           |225              |Kwun Ho So            |1023  |
|21  |Colt Love             |224              |Robert Zhongjia Shi   |1000  |
|22  |Andrew Meijer         |224              |Sarabpreet Singh Sodhi|1000  |
|23  |Brendon Kwan          |224              |Kelsey Liang          |1000  |
|24  |Samuel Ha             |224              |Robert Stephen Foster |996   |
|25  |Laurence Kao          |175              |Maurice Li            |992   |
|26  |Robert Zhongjia Shi   |132              |Allan Crawford        |992   |
|27  |William Ka wang Ma    |132              |William Ka wang Ma    |992   |
|28  |Kelsey Liang          |132              |Angus Li              |985   |
|29  |John Ou               |132              |Andrew Meijer         |977   |
|30  |Angus Li              |132              |Laurence Kao          |956   |
|31  |Sarabpreet Singh Sodhi|132              |Arseny Shestakov      |956   |
|32  |Allan Crawford        |132              |Aakar Chatha          |954   |
|33  |Maurice Li            |132              |Dayton Se             |950   |
|34  |Nicholas Poon         |49               |Oliver Long           |947   |
|35  |Justin Lam            |49               |Zhengheng Bao         |942   |
|36  |Oliver Long           |49               |Sahil Rajesh Aggarwal |936   |
|37  |Ayden Travis Lee      |49               |John Ou               |935   |
|38  |Marcus James Tseng    |49               |Roy Hung              |912   |
|39  |Aakar Chatha          |49               |Colt Love             |911   |
|40  |Andy Le               |49               |Renjie Xiong          |907   |
|41  |Arseny Shestakov      |49               |Justin Lam            |907   |
|42  |Hossein Ahmadi        |49               |Yichen Li             |907   |
|43  |Luca Ferretti         |49               |Andy Le               |905   |
|44  |Robert Stephen Foster |49               |Bangjian (James) Geng |905   |
|45  |Dwayne Da Silva       |49               |Hossein Ahmadi        |901   |
|46  |Renjie Xiong          |49               |Luca Ferretti         |901   |
|47  |Zhengheng Bao         |49               |Dwayne Da Silva       |901   |
|48  |Yichen Li             |49               |Marcus James Tseng    |900   |
|49  |Yancong Li            |49               |Ayush Ayush           |896   |
|50  |Bangjian (James) Geng |49               |Samuel Ha             |850   |
|51  |Dayton Se             |0                |Brendon Kwan          |843   |


### Variations
 - Changing K value based on consolation
 - Changing K value based on streakiness/round/depth (this emphasizes the reduced K value in consolation Variation 1)
 - Using function of tournament points as initial ranking
 - Changing K value based on number of games in the match (if you go three games and get to extra points in the third, you don't lose as much ranking).
 - Combined Variation (combining all previous variations)
 - Changing K value based on the tournament type (see Badminton BC page for how that works on tournament points)
 - Reducing K value based on number of tournaments played

### Prototype No.2 consolationFix.py: Lower K Value For Consolation
In the current tournament ruleset, if a player loses their first match in the Single Elimination bracket, they are eligible for Consolation bracket, so every player can play two matches. This creates a problem for my ranking system where players who do well in consolation end up getting over-ranked. The problem of consolation matches would be solved automatically by switching to a Double Elimination format, but as it is, this problem can be solved by first separating each tournament into its own CSV file. Suppose that a Consolation champion shouldn't gain as much ranking as a player who wins their first round match. To do this, consolationFix.py divides the default constant K value by the number of Consolation rounds. For a bracket of 16 players, there are 3 rounds; for a bracket of 32 players, there are 4 rounds; for a bracket of 64 players, there are 5 rounds, and so on. The point is that the K value is lower in consolation so that consolation matches do not affect rating as much.
 - 2024Tournament_JackUnderhill.csv (Deprecated)
 - 2024Tournament_Provincials.csv (deprecated)
 - 2024TournamentScores_JackUnderHill.csv (includes games scores for Prototype No.4)
 - 2024TournamentScores_Provincials.csv (includes games scores for Prototype No.4)
 
This variation adds a boolean variable to the Player object to track whether or not the player is in consolation (defaults to False). When rating changes are being assigned, the program checks if the players are in consolation by using these varaibles. Also, whenever a player loses a match, the program sets their consolation boolean to True. Since this version of the program runs separately for each tournament, these booleans are reset to False when the Players are reinitialized for each tournament.

#### Prototype No.2 Results
Running consolationFix.py first on the Jack Underhill match data and then on the Provincial Championships match data yielded results that make sense: the consolation players are now all lower rated. A side effect of this variation is that all players now have lower ratings.

|Rank|Official Rankings     |Tournament Points|Consolation Fix       |Rating|
|----|----------------------|-----------------|----------------------|------|
|1   |Saurabh Pandiar       |1488             |Saurabh Pandiar       |1347  |
|2   |Simar Singh           |935              |Simar Singh           |1165  |
|3   |Jalil Waiz            |930              |Lyem Fedoretz         |1163  |
|4   |Jack Chen             |810              |Victor Ho             |1116  |
|5   |Connor Nicholas Louie |805              |Jack Chen             |1116  |
|6   |Kwun Ho So            |685              |Ryan Liu              |1109  |
|7   |Lyem Fedoretz         |533              |Anish Chandra Jojula  |1087  |
|8   |Uday Pratap Bharti    |520              |Stephen Dee           |1075  |
|9   |Sahil Rajesh Aggarwal |509              |Connor Nicholas Louie |1050  |
|10  |Ratnesh Rao Ippili    |509              |Shingchun (Kevin) Wu  |1043  |
|11  |Victor Ho             |439              |Rickey Ruixi Zhang    |1042  |
|12  |Ryan Liu              |439              |Jasper Kong           |1036  |
|13  |Roy Hung              |400              |Angus Li              |1033  |
|14  |Anish Chandra Jojula  |345              |Uday Pratap Bharti    |1032  |
|15  |Jaden Thom            |307              |Kwun Ho So            |1026  |
|16  |Ayush Ayush           |307              |Jalil Waiz            |1022  |
|17  |Rickey Ruixi Zhang    |225              |Nicholas Poon         |1010  |
|18  |Shingchun (Kevin) Wu  |225              |Jaden Thom            |1003  |
|19  |Jasper Kong           |225              |Robert Zhongjia Shi   |1000  |
|20  |Stephen Dee           |225              |Sarabpreet Singh Sodhi|1000  |
|21  |Colt Love             |224              |Kelsey Liang          |1000  |
|22  |Andrew Meijer         |224              |Maurice Li            |992   |
|23  |Brendon Kwan          |224              |Allan Crawford        |992   |
|24  |Samuel Ha             |224              |William Ka wang Ma    |992   |
|25  |Laurence Kao          |175              |John Ou               |977   |
|26  |Robert Zhongjia Shi   |132              |Ayden Travis Lee      |975   |
|27  |William Ka wang Ma    |132              |Yancong Li            |973   |
|28  |Kelsey Liang          |132              |Sahil Rajesh Aggarwal |970   |
|29  |John Ou               |132              |Ratnesh Rao Ippili    |967   |
|30  |Angus Li              |132              |Robert Stephen Foster |967   |
|31  |Sarabpreet Singh Sodhi|132              |Laurence Kao          |956   |
|32  |Allan Crawford        |132              |Aakar Chatha          |956   |
|33  |Maurice Li            |132              |Oliver Long           |955   |
|34  |Nicholas Poon         |49               |Dayton Se             |950   |
|35  |Justin Lam            |49               |Arseny Shestakov      |949   |
|36  |Oliver Long           |49               |Zhengheng Bao         |949   |
|37  |Ayden Travis Lee      |49               |Andy Le               |944   |
|38  |Marcus James Tseng    |49               |Bangjian (James) Geng |944   |
|39  |Aakar Chatha          |49               |Renjie Xiong          |938   |
|40  |Andy Le               |49               |Yichen Li             |938   |
|41  |Arseny Shestakov      |49               |Justin Lam            |937   |
|42  |Hossein Ahmadi        |49               |Hossein Ahmadi        |937   |
|43  |Luca Ferretti         |49               |Luca Ferretti         |937   |
|44  |Robert Stephen Foster |49               |Dwayne Da Silva       |937   |
|45  |Dwayne Da Silva       |49               |Marcus James Tseng    |937   |
|46  |Renjie Xiong          |49               |Roy Hung              |936   |
|47  |Zhengheng Bao         |49               |Ayush Ayush           |936   |
|48  |Yichen Li             |49               |Colt Love             |919   |
|49  |Yancong Li            |49               |Andrew Meijer         |919   |
|50  |Bangjian (James) Geng |49               |Brendon Kwan          |890   |
|51  |Dayton Se             |0                |Samuel Ha             |887   |


### Prototype No.3 winningStreaks.py: Higher K Value For Winning Streaks
Now that we have a K value that changes based on the match results for each player, this principle can be applied in reverse, increasing the k value for the main draw. Getting deep into a tournament bracket should empower players to win more ELO, and this contrasts with the lower K value in Consolation. 
To implement this, I add a new variable to the Player Class called winningStreak. I add to winningStreak whenever a player wins a game. When a player wins a game, add winningStreak*(k/r) to the K value where k is the initial K value and r is the number of rounds in the tournament. Thus, by the finals, the K value should be double what it started at. 

#### Prototype No.3 Results
outputVariation2.py has a similar effect to the original prototype where consolation players are overranked, and we can expect to see this in the results of the combined variation. Seems to be working -- onto the next.

|Rank|Official Rankings     |Tournament Points|Variation 2           |Rating|
|----|----------------------|-----------------|----------------------|------|
|1   |Saurabh Pandiar       |1488             |Saurabh Pandiar       |1486  |
|2   |Simar Singh           |935              |Nicholas Poon         |1302  |
|3   |Jalil Waiz            |930              |Simar Singh           |1253  |
|4   |Jack Chen             |810              |Lyem Fedoretz         |1247  |
|5   |Connor Nicholas Louie |805              |Victor Ho             |1163  |
|6   |Kwun Ho So            |685              |Jack Chen             |1151  |
|7   |Lyem Fedoretz         |533              |Ryan Liu              |1149  |
|8   |Uday Pratap Bharti    |520              |Jaden Thom            |1135  |
|9   |Sahil Rajesh Aggarwal |509              |Anish Chandra Jojula  |1120  |
|10  |Ratnesh Rao Ippili    |509              |Jalil Waiz            |1114  |
|11  |Victor Ho             |439              |Ayden Travis Lee      |1112  |
|12  |Ryan Liu              |439              |Uday Pratap Bharti    |1062  |
|13  |Roy Hung              |400              |Connor Nicholas Louie |1062  |
|14  |Anish Chandra Jojula  |345              |Yancong Li            |1060  |
|15  |Jaden Thom            |307              |Ratnesh Rao Ippili    |1058  |
|16  |Ayush Ayush           |307              |Shingchun (Kevin) Wu  |1054  |
|17  |Rickey Ruixi Zhang    |225              |Rickey Ruixi Zhang    |1053  |
|18  |Shingchun (Kevin) Wu  |225              |Jasper Kong           |1046  |
|19  |Jasper Kong           |225              |Stephen Dee           |1040  |
|20  |Stephen Dee           |225              |Kwun Ho So            |1032  |
|21  |Colt Love             |224              |Robert Stephen Foster |1006  |
|22  |Andrew Meijer         |224              |Robert Zhongjia Shi   |1000  |
|23  |Brendon Kwan          |224              |Sarabpreet Singh Sodhi|1000  |
|24  |Samuel Ha             |224              |Kelsey Liang          |1000  |
|25  |Laurence Kao          |175              |Andrew Meijer         |995   |
|26  |Robert Zhongjia Shi   |132              |Maurice Li            |992   |
|27  |William Ka wang Ma    |132              |Allan Crawford        |992   |
|28  |Kelsey Liang          |132              |William Ka wang Ma    |992   |
|29  |John Ou               |132              |Angus Li              |985   |
|30  |Angus Li              |132              |Laurence Kao          |957   |
|31  |Sarabpreet Singh Sodhi|132              |Arseny Shestakov      |956   |
|32  |Allan Crawford        |132              |Aakar Chatha          |954   |
|33  |Maurice Li            |132              |Dayton Se             |950   |
|34  |Nicholas Poon         |49               |Oliver Long           |947   |
|35  |Justin Lam            |49               |Zhengheng Bao         |942   |
|36  |Oliver Long           |49               |Sahil Rajesh Aggarwal |942   |
|37  |Ayden Travis Lee      |49               |John Ou               |935   |
|38  |Marcus James Tseng    |49               |Colt Love             |921   |
|39  |Aakar Chatha          |49               |Roy Hung              |914   |
|40  |Andy Le               |49               |Renjie Xiong          |907   |
|41  |Arseny Shestakov      |49               |Justin Lam            |907   |
|42  |Hossein Ahmadi        |49               |Yichen Li             |907   |
|43  |Luca Ferretti         |49               |Andy Le               |905   |
|44  |Robert Stephen Foster |49               |Bangjian (James) Geng |905   |
|45  |Dwayne Da Silva       |49               |Hossein Ahmadi        |901   |
|46  |Renjie Xiong          |49               |Luca Ferretti         |901   |
|47  |Zhengheng Bao         |49               |Dwayne Da Silva       |901   |
|48  |Yichen Li             |49               |Marcus James Tseng    |900   |
|49  |Yancong Li            |49               |Ayush Ayush           |899   |
|50  |Bangjian (James) Geng |49               |Samuel Ha             |850   |
|51  |Dayton Se             |0                |Brendon Kwan          |846   |


### Prototype No.4 closeMatchVariation.py: Going Three Games
Prototype No.2 requires changing the K value equally for both players, Prototype No.3 requires changing the K value for the winning player, and Prototype No.4 requires changing the K value for the losing player. This variation also requires changing the input data so that the match scores are included. Players that lose in three games in a ranked match and get to extra points in the third game should lose half as much rating because it is such a close match. After creating the new CSV files, I realized a small error in the CSV files I was using earlier: one of the matches was in the wrong tournament. Now fixed, I will recreate the output files with the correct data once all the variations are finished. There are a few matches from the Jack Underhill and Provincial Championships that went to extra points in the third game.

At first, I thought this sort of use-case called for regex, but it seems simple enough to puzzle out with a little experimentation. The split() function should work nicely for this.
 - 2024Tournament_JackUnderhill.csv (Deprecated)
 - 2024Tournament_Provincials.csv (deprecated)
 - 2024TournamentScores_JackUnderHill.csv (includes games scores for Prototype No.4)
 - 2024TournamentScores_Provincials.csv (includes games scores for Prototype No.4)

#### Prototype No.4 Results
I used a print statement to test that the selection was working properly before moving on from this variation. Fortunately, there was one match in each of the two events that went to extra points in the third game. A direct comparison with the output from the initial prototype shows that Sarabpreet Singh Sodhi (+25) and Uday Pratap Bharti (+20) both have slightly higher ratings because of this variation. Other players also have slight changes too as a side effect of this.\

|Rank|Official Rankings     |Tournament Points|Variation 3           |Rating|
|----|----------------------|-----------------|----------------------|------|
|1   |Saurabh Pandiar       |1488             |Saurabh Pandiar       |1354  |
|2   |Simar Singh           |935              |Nicholas Poon         |1192  |
|3   |Jalil Waiz            |930              |Simar Singh           |1180  |
|4   |Jack Chen             |810              |Lyem Fedoretz         |1165  |
|5   |Connor Nicholas Louie |805              |Jack Chen             |1143  |
|6   |Kwun Ho So            |685              |Victor Ho             |1116  |
|7   |Lyem Fedoretz         |533              |Ryan Liu              |1112  |
|8   |Uday Pratap Bharti    |520              |Jaden Thom            |1097  |
|9   |Sahil Rajesh Aggarwal |509              |Anish Chandra Jojula  |1087  |
|10  |Ratnesh Rao Ippili    |509              |Ayden Travis Lee      |1065  |
|11  |Victor Ho             |439              |Uday Pratap Bharti    |1052  |
|12  |Ryan Liu              |439              |Jalil Waiz            |1050  |
|13  |Roy Hung              |400              |Connor Nicholas Louie |1050  |
|14  |Anish Chandra Jojula  |345              |Shingchun (Kevin) Wu  |1043  |
|15  |Jaden Thom            |307              |Rickey Ruixi Zhang    |1042  |
|16  |Ayush Ayush           |307              |Jasper Kong           |1036  |
|17  |Rickey Ruixi Zhang    |225              |Stephen Dee           |1036  |
|18  |Shingchun (Kevin) Wu  |225              |Ratnesh Rao Ippili    |1034  |
|19  |Jasper Kong           |225              |Yancong Li            |1032  |
|20  |Stephen Dee           |225              |Sarabpreet Singh Sodhi|1025  |
|21  |Colt Love             |224              |Kwun Ho So            |1018  |
|22  |Andrew Meijer         |224              |Kelsey Liang          |1000  |
|23  |Brendon Kwan          |224              |Robert Stephen Foster |996   |
|24  |Samuel Ha             |224              |Robert Zhongjia Shi   |992   |
|25  |Laurence Kao          |175              |Angus Li              |992   |
|26  |Robert Zhongjia Shi   |132              |Maurice Li            |992   |
|27  |William Ka wang Ma    |132              |Allan Crawford        |992   |
|28  |Kelsey Liang          |132              |William Ka wang Ma    |992   |
|29  |John Ou               |132              |Andrew Meijer         |977   |
|30  |Angus Li              |132              |Laurence Kao          |956   |
|31  |Sarabpreet Singh Sodhi|132              |Arseny Shestakov      |956   |
|32  |Allan Crawford        |132              |Aakar Chatha          |954   |
|33  |Maurice Li            |132              |Dayton Se             |950   |
|34  |Nicholas Poon         |49               |Oliver Long           |947   |
|35  |Justin Lam            |49               |Zhengheng Bao         |942   |
|36  |Oliver Long           |49               |Sahil Rajesh Aggarwal |936   |
|37  |Ayden Travis Lee      |49               |John Ou               |935   |
|38  |Marcus James Tseng    |49               |Roy Hung              |915   |
|39  |Aakar Chatha          |49               |Colt Love             |911   |
|40  |Andy Le               |49               |Renjie Xiong          |907   |
|41  |Arseny Shestakov      |49               |Justin Lam            |907   |
|42  |Hossein Ahmadi        |49               |Yichen Li             |907   |
|43  |Luca Ferretti         |49               |Andy Le               |905   |
|44  |Robert Stephen Foster |49               |Bangjian (James) Geng |905   |
|45  |Dwayne Da Silva       |49               |Hossein Ahmadi        |901   |
|46  |Renjie Xiong          |49               |Luca Ferretti         |901   |
|47  |Zhengheng Bao         |49               |Dwayne Da Silva       |901   |
|48  |Yichen Li             |49               |Marcus James Tseng    |900   |
|49  |Yancong Li            |49               |Ayush Ayush           |896   |
|50  |Bangjian (James) Geng |49               |Samuel Ha             |850   |
|51  |Dayton Se             |0                |Brendon Kwan          |844   |


### Prototype No.5 pointsVariation.py: Tournament Points As Initial Ranking
So far, all of the variations have started with each player rated at 1000 ELO rating points. Why not initialize the players with an average of 1000 and their tournament points from the official rankings? It is an intuitive place to start, to get a rough idea of the player levels. This is very simple to implement since I have a CSV file with the tournament points for each player already prepared. I created an intermediary file called sourceRankings.py with a program called makeSourceRankings.py. All I did was take each rating from officialRankings.py and average it with 1000 to neutralize the large disparity (since the official Rankings are based on tournament points). Now I can use the new file sourceRankings.py for this variation, the combined variation, and future testing.

#### Prototype No.5 Results
This variation was a little finicky at first, because I had to correct my input to ensure the names of all the players matched with the inputRankings.csv file I've been using. Dayton was not in the official rankings even though he attended the Jack Underhill, and the reason for this is because he was walked over in his first match of the Jack Underhill, and never played any matches. I added him to the official rankings with zero tournament points. This set his starting source rating (in sourceRankings.csv) to 500. Initializing the algorithm with the official Badminton BC rankings did a good job of reducing the amount by which consolation players are overrated. One strange effect of this variation is that Nicholas Poon still managed to outrank Anish Jojula even though Nicholas lost to Anish in the first round.

|Rank|Official Rankings     |Tournament Points|Variation 4           |Rating|
|----|----------------------|-----------------|----------------------|------|
|1   |Saurabh Pandiar       |1488             |Saurabh Pandiar       |1324  |
|2   |Simar Singh           |935              |Simar Singh           |1012  |
|3   |Jalil Waiz            |930              |Jack Chen             |987   |
|4   |Jack Chen             |810              |Lyem Fedoretz         |917   |
|5   |Connor Nicholas Louie |805              |Jalil Waiz            |901   |
|6   |Kwun Ho So            |685              |Ryan Liu              |863   |
|7   |Lyem Fedoretz         |533              |Connor Nicholas Louie |849   |
|8   |Uday Pratap Bharti    |520              |Victor Ho             |839   |
|9   |Sahil Rajesh Aggarwal |509              |Kwun Ho So            |822   |
|10  |Ratnesh Rao Ippili    |509              |Uday Pratap Bharti    |783   |
|11  |Victor Ho             |439              |Jaden Thom            |756   |
|12  |Ryan Liu              |439              |Nicholas Poon         |755   |
|13  |Roy Hung              |400              |Anish Chandra Jojula  |729   |
|14  |Anish Chandra Jojula  |345              |Ratnesh Rao Ippili    |712   |
|15  |Jaden Thom            |307              |Stephen Dee           |665   |
|16  |Ayush Ayush           |307              |Jasper Kong           |658   |
|17  |Rickey Ruixi Zhang    |225              |Sahil Rajesh Aggarwal |656   |
|18  |Shingchun (Kevin) Wu  |225              |Shingchun (Kevin) Wu  |654   |
|19  |Jasper Kong           |225              |Rickey Ruixi Zhang    |637   |
|20  |Stephen Dee           |225              |Roy Hung              |633   |
|21  |Colt Love             |224              |Sarabpreet Singh Sodhi|627   |
|22  |Andrew Meijer         |224              |Allan Crawford        |619   |
|23  |Brendon Kwan          |224              |Ayden Travis Lee      |609   |
|24  |Samuel Ha             |224              |Angus Li              |597   |
|25  |Laurence Kao          |175              |Andrew Meijer         |594   |
|26  |Robert Zhongjia Shi   |132              |Robert Zhongjia Shi   |593   |
|27  |William Ka wang Ma    |132              |William Ka wang Ma    |585   |
|28  |Kelsey Liang          |132              |Robert Stephen Foster |583   |
|29  |John Ou               |132              |Kelsey Liang          |575   |
|30  |Angus Li              |132              |Yancong Li            |575   |
|31  |Sarabpreet Singh Sodhi|132              |Laurence Kao          |573   |
|32  |Allan Crawford        |132              |Maurice Li            |571   |
|33  |Maurice Li            |132              |Ayush Ayush           |559   |
|34  |Nicholas Poon         |49               |John Ou               |524   |
|35  |Justin Lam            |49               |Colt Love             |521   |
|36  |Oliver Long           |49               |Oliver Long           |509   |
|37  |Ayden Travis Lee      |49               |Arseny Shestakov      |497   |
|38  |Marcus James Tseng    |49               |Aakar Chatha          |490   |
|39  |Aakar Chatha          |49               |Marcus James Tseng    |487   |
|40  |Andy Le               |49               |Zhengheng Bao         |487   |
|41  |Arseny Shestakov      |49               |Brendon Kwan          |485   |
|42  |Hossein Ahmadi        |49               |Samuel Ha             |463   |
|43  |Luca Ferretti         |49               |Luca Ferretti         |460   |
|44  |Robert Stephen Foster |49               |Dayton Se             |459   |
|45  |Dwayne Da Silva       |49               |Renjie Xiong          |456   |
|46  |Renjie Xiong          |49               |Dwayne Da Silva       |447   |
|47  |Zhengheng Bao         |49               |Andy Le               |446   |
|48  |Yichen Li             |49               |Yichen Li             |444   |
|49  |Yancong Li            |49               |Bangjian (James) Geng |440   |
|50  |Bangjian (James) Geng |49               |Justin Lam            |437   |
|51  |Dayton Se             |0                |Hossein Ahmadi        |436   |


### Prototype No.6 combinedVariation.py: Combining All Four Above Variations
Combining all four previous variations should produce a more accurate ranking than any of the previous variations on their own.
 - Add consolation = False to Player object
 - Add winningStreak = 0 to Player object
 - Use separate variables LK and WK.
 - Implement the closeMatchVariation algorithm
 - Add consolation variables check (and update k value)
 - Add consolation variables update
 - Add winningStreak variable updates
 - Add winningStreak variable checks (and update k value)
 - set input rankings to sourceRankings.csv
 - run on 2024TournamentScores_JackUnderHill.csv and output to an intermediary file
 - set input rankings to the intermediary file
 - run on 2024TournamentScores_Provincials.csv and output to outputVariation5.csv

#### Prototype No.6 Results
The results look good but I also want to see what they would look like if I used a blank initial ranking where everyone starts with 1000 ELO points, instead of using the official rankings to initialize.

#### Prototype No.6 Results 2
It's hard to say exactly which of the two rankings is better between outputVariation5.csv and outputVariation6.csv, but I like outputVariation6.csv better because it does not take tournament placement into account at all, it is not biased on favour of the official rankings, and yet it produces a very accurate ranking. I am looking forward to testing out this system on more match data.

#### Prototype No.6 Comparison to Official Rankings
|Rank|Official Rankings     |Tournament Points|Combined Variation    |Rating|Variation 6           |Rating|
|----|----------------------|-----------------|----------------------|------|----------------------|------|
|1   |Saurabh Pandiar       |1488             |Saurabh Pandiar       |1384  |Saurabh Pandiar       |1486  |
|2   |Simar Singh           |935              |Simar Singh           |1074  |Simar Singh           |1251  |
|3   |Jalil Waiz            |930              |Lyem Fedoretz         |991   |Lyem Fedoretz         |1247  |
|4   |Jack Chen             |810              |Jack Chen             |964   |Victor Ho             |1162  |
|5   |Connor Nicholas Louie |805              |Jalil Waiz            |950   |Ryan Liu              |1151  |
|6   |Kwun Ho So            |685              |Ryan Liu              |907   |Jack Chen             |1133  |
|7   |Lyem Fedoretz         |533              |Victor Ho             |888   |Anish Chandra Jojula  |1120  |
|8   |Uday Pratap Bharti    |520              |Connor Nicholas Louie |855   |Jalil Waiz            |1105  |
|9   |Sahil Rajesh Aggarwal |509              |Uday Pratap Bharti    |837   |Uday Pratap Bharti    |1080  |
|10  |Ratnesh Rao Ippili    |509              |Kwun Ho So            |828   |Connor Nicholas Louie |1062  |
|11  |Victor Ho             |439              |Anish Chandra Jojula  |756   |Shingchun (Kevin) Wu  |1054  |
|12  |Ryan Liu              |439              |Sahil Rajesh Aggarwal |712   |Rickey Ruixi Zhang    |1053  |
|13  |Roy Hung              |400              |Ratnesh Rao Ippili    |701   |Jasper Kong           |1046  |
|14  |Anish Chandra Jojula  |345              |Roy Hung              |677   |Stephen Dee           |1046  |
|15  |Jaden Thom            |307              |Jaden Thom            |674   |Nicholas Poon         |1040  |
|16  |Ayush Ayush           |307              |Stephen Dee           |672   |Kwun Ho So            |1029  |
|17  |Rickey Ruixi Zhang    |225              |Jasper Kong           |668   |Sarabpreet Singh Sodhi|1025  |
|18  |Shingchun (Kevin) Wu  |225              |Shingchun (Kevin) Wu  |664   |Jaden Thom            |1019  |
|19  |Jasper Kong           |225              |Rickey Ruixi Zhang    |645   |Kelsey Liang          |1000  |
|20  |Stephen Dee           |225              |Sarabpreet Singh Sodhi|633   |Robert Zhongjia Shi   |992   |
|21  |Colt Love             |224              |Allan Crawford        |619   |Angus Li              |992   |
|22  |Andrew Meijer         |224              |Ayush Ayush           |608   |Maurice Li            |992   |
|23  |Brendon Kwan          |224              |Angus Li              |597   |Allan Crawford        |992   |
|24  |Samuel Ha             |224              |Nicholas Poon         |595   |William Ka wang Ma    |992   |
|25  |Laurence Kao          |175              |Robert Zhongjia Shi   |593   |Ratnesh Rao Ippili    |990   |
|26  |Robert Zhongjia Shi   |132              |William Ka wang Ma    |585   |Ayden Travis Lee      |986   |
|27  |William Ka wang Ma    |132              |Kelsey Liang          |575   |Yancong Li            |980   |
|28  |Kelsey Liang          |132              |Laurence Kao          |573   |Sahil Rajesh Aggarwal |978   |
|29  |John Ou               |132              |John Ou               |573   |John Ou               |977   |
|30  |Angus Li              |132              |Maurice Li            |571   |Robert Stephen Foster |970   |
|31  |Sarabpreet Singh Sodhi|132              |Colt Love             |546   |Laurence Kao          |957   |
|32  |Allan Crawford        |132              |Andrew Meijer         |542   |Aakar Chatha          |956   |
|33  |Maurice Li            |132              |Robert Stephen Foster |530   |Oliver Long           |955   |
|34  |Nicholas Poon         |49               |Brendon Kwan          |523   |Roy Hung              |954   |
|35  |Justin Lam            |49               |Ayden Travis Lee      |519   |Dayton Se             |950   |
|36  |Oliver Long           |49               |Yancong Li            |519   |Arseny Shestakov      |949   |
|37  |Ayden Travis Lee      |49               |Oliver Long           |511   |Zhengheng Bao         |949   |
|38  |Marcus James Tseng    |49               |Samuel Ha             |509   |Andy Le               |944   |
|39  |Aakar Chatha          |49               |Marcus James Tseng    |508   |Bangjian (James) Geng |944   |
|40  |Andy Le               |49               |Luca Ferretti         |497   |Ayush Ayush           |938   |
|41  |Arseny Shestakov      |49               |Aakar Chatha          |490   |Renjie Xiong          |938   |
|42  |Hossein Ahmadi        |49               |Arseny Shestakov      |490   |Yichen Li             |938   |
|43  |Luca Ferretti         |49               |Zhengheng Bao         |487   |Justin Lam            |937   |
|44  |Robert Stephen Foster |49               |Andy Le               |484   |Hossein Ahmadi        |937   |
|45  |Dwayne Da Silva       |49               |Renjie Xiong          |481   |Luca Ferretti         |937   |
|46  |Renjie Xiong          |49               |Bangjian (James) Geng |478   |Dwayne Da Silva       |937   |
|47  |Zhengheng Bao         |49               |Dwayne Da Silva       |476   |Marcus James Tseng    |937   |
|48  |Yichen Li             |49               |Hossein Ahmadi        |473   |Andrew Meijer         |924   |
|49  |Yancong Li            |49               |Yichen Li             |469   |Colt Love             |923   |
|50  |Bangjian (James) Geng |49               |Justin Lam            |468   |Brendon Kwan          |892   |
|51  |Dayton Se             |0                |Dayton Se             |459   |Samuel Ha             |887   |


### Prototype No.7 advancedVariation.py: Tournament Type, Tournaments Played, and High Ratings
This prototype will be made in preparation for adding more tournaments and match data.

This variation should also implement additional features such as saving and exporting Player variables to the rankings file so that players can carry their win streaks between tournaments. There are a lot of small features that can be added to optimize the system in preparation for a lot of match data.

### Variations Compared to Official Rankings
|Rank|Official Rankings     |Tournament Points|Initial Prototype     |Rating|Consolation Fix       |Rating|Variation 2           |Rating|Variation 3           |Rating|Variation 4           |Rating|Combined Variation    |Rating|Variation 6           |Rating|
|----|----------------------|-----------------|----------------------|------|----------------------|------|----------------------|------|----------------------|------|----------------------|------|----------------------|------|----------------------|------|
|1   |Saurabh Pandiar       |1488             |Saurabh Pandiar       |1352  |Saurabh Pandiar       |1347  |Saurabh Pandiar       |1486  |Saurabh Pandiar       |1354  |Saurabh Pandiar       |1324  |Saurabh Pandiar       |1384  |Saurabh Pandiar       |1486  |
|2   |Simar Singh           |935              |Nicholas Poon         |1192  |Simar Singh           |1165  |Nicholas Poon         |1302  |Nicholas Poon         |1192  |Simar Singh           |1012  |Simar Singh           |1074  |Simar Singh           |1251  |
|3   |Jalil Waiz            |930              |Simar Singh           |1176  |Lyem Fedoretz         |1163  |Simar Singh           |1253  |Simar Singh           |1180  |Jack Chen             |987   |Lyem Fedoretz         |991   |Lyem Fedoretz         |1247  |
|4   |Jack Chen             |810              |Lyem Fedoretz         |1164  |Victor Ho             |1116  |Lyem Fedoretz         |1247  |Lyem Fedoretz         |1165  |Lyem Fedoretz         |917   |Jack Chen             |964   |Victor Ho             |1162  |
|5   |Connor Nicholas Louie |805              |Victor Ho             |1116  |Jack Chen             |1116  |Victor Ho             |1163  |Jack Chen             |1143  |Jalil Waiz            |901   |Jalil Waiz            |950   |Ryan Liu              |1151  |
|6   |Kwun Ho So            |685              |Jack Chen             |1116  |Ryan Liu              |1109  |Jack Chen             |1151  |Victor Ho             |1116  |Ryan Liu              |863   |Ryan Liu              |907   |Jack Chen             |1133  |
|7   |Lyem Fedoretz         |533              |Ryan Liu              |1111  |Anish Chandra Jojula  |1087  |Ryan Liu              |1149  |Ryan Liu              |1112  |Connor Nicholas Louie |849   |Victor Ho             |888   |Anish Chandra Jojula  |1120  |
|8   |Uday Pratap Bharti    |520              |Jaden Thom            |1097  |Stephen Dee           |1075  |Jaden Thom            |1135  |Jaden Thom            |1097  |Victor Ho             |839   |Connor Nicholas Louie |855   |Jalil Waiz            |1105  |
|9   |Sahil Rajesh Aggarwal |509              |Anish Chandra Jojula  |1087  |Connor Nicholas Louie |1050  |Anish Chandra Jojula  |1120  |Anish Chandra Jojula  |1087  |Kwun Ho So            |822   |Uday Pratap Bharti    |837   |Uday Pratap Bharti    |1080  |
|10  |Ratnesh Rao Ippili    |509              |Jalil Waiz            |1082  |Shingchun (Kevin) Wu  |1043  |Jalil Waiz            |1114  |Ayden Travis Lee      |1065  |Uday Pratap Bharti    |783   |Kwun Ho So            |828   |Connor Nicholas Louie |1062  |
|11  |Victor Ho             |439              |Ayden Travis Lee      |1065  |Rickey Ruixi Zhang    |1042  |Ayden Travis Lee      |1112  |Uday Pratap Bharti    |1052  |Jaden Thom            |756   |Anish Chandra Jojula  |756   |Shingchun (Kevin) Wu  |1054  |
|12  |Ryan Liu              |439              |Connor Nicholas Louie |1050  |Jasper Kong           |1036  |Uday Pratap Bharti    |1062  |Jalil Waiz            |1050  |Nicholas Poon         |755   |Sahil Rajesh Aggarwal |712   |Rickey Ruixi Zhang    |1053  |
|13  |Roy Hung              |400              |Shingchun (Kevin) Wu  |1043  |Angus Li              |1033  |Connor Nicholas Louie |1062  |Connor Nicholas Louie |1050  |Anish Chandra Jojula  |729   |Ratnesh Rao Ippili    |701   |Jasper Kong           |1046  |
|14  |Anish Chandra Jojula  |345              |Rickey Ruixi Zhang    |1042  |Uday Pratap Bharti    |1032  |Yancong Li            |1060  |Shingchun (Kevin) Wu  |1043  |Ratnesh Rao Ippili    |712   |Roy Hung              |677   |Stephen Dee           |1046  |
|15  |Jaden Thom            |307              |Jasper Kong           |1036  |Kwun Ho So            |1026  |Ratnesh Rao Ippili    |1058  |Rickey Ruixi Zhang    |1042  |Stephen Dee           |665   |Jaden Thom            |674   |Nicholas Poon         |1040  |
|16  |Ayush Ayush           |307              |Uday Pratap Bharti    |1032  |Jalil Waiz            |1022  |Shingchun (Kevin) Wu  |1054  |Jasper Kong           |1036  |Jasper Kong           |658   |Stephen Dee           |672   |Kwun Ho So            |1029  |
|17  |Rickey Ruixi Zhang    |225              |Yancong Li            |1032  |Nicholas Poon         |1010  |Rickey Ruixi Zhang    |1053  |Stephen Dee           |1036  |Sahil Rajesh Aggarwal |656   |Jasper Kong           |668   |Sarabpreet Singh Sodhi|1025  |
|18  |Shingchun (Kevin) Wu  |225              |Ratnesh Rao Ippili    |1030  |Jaden Thom            |1003  |Jasper Kong           |1046  |Ratnesh Rao Ippili    |1034  |Shingchun (Kevin) Wu  |654   |Shingchun (Kevin) Wu  |664   |Jaden Thom            |1019  |
|19  |Jasper Kong           |225              |Stephen Dee           |1030  |Robert Zhongjia Shi   |1000  |Stephen Dee           |1040  |Yancong Li            |1032  |Rickey Ruixi Zhang    |637   |Rickey Ruixi Zhang    |645   |Kelsey Liang          |1000  |
|20  |Stephen Dee           |225              |Kwun Ho So            |1023  |Sarabpreet Singh Sodhi|1000  |Kwun Ho So            |1032  |Sarabpreet Singh Sodhi|1025  |Roy Hung              |633   |Sarabpreet Singh Sodhi|633   |Robert Zhongjia Shi   |992   |
|21  |Colt Love             |224              |Robert Zhongjia Shi   |1000  |Kelsey Liang          |1000  |Robert Stephen Foster |1006  |Kwun Ho So            |1018  |Sarabpreet Singh Sodhi|627   |Allan Crawford        |619   |Angus Li              |992   |
|22  |Andrew Meijer         |224              |Sarabpreet Singh Sodhi|1000  |Maurice Li            |992   |Robert Zhongjia Shi   |1000  |Kelsey Liang          |1000  |Allan Crawford        |619   |Ayush Ayush           |608   |Maurice Li            |992   |
|23  |Brendon Kwan          |224              |Kelsey Liang          |1000  |Allan Crawford        |992   |Sarabpreet Singh Sodhi|1000  |Robert Stephen Foster |996   |Ayden Travis Lee      |609   |Angus Li              |597   |Allan Crawford        |992   |
|24  |Samuel Ha             |224              |Robert Stephen Foster |996   |William Ka wang Ma    |992   |Kelsey Liang          |1000  |Robert Zhongjia Shi   |992   |Angus Li              |597   |Nicholas Poon         |595   |William Ka wang Ma    |992   |
|25  |Laurence Kao          |175              |Maurice Li            |992   |John Ou               |977   |Andrew Meijer         |995   |Angus Li              |992   |Andrew Meijer         |594   |Robert Zhongjia Shi   |593   |Ratnesh Rao Ippili    |990   |
|26  |Robert Zhongjia Shi   |132              |Allan Crawford        |992   |Ayden Travis Lee      |975   |Maurice Li            |992   |Maurice Li            |992   |Robert Zhongjia Shi   |593   |William Ka wang Ma    |585   |Ayden Travis Lee      |986   |
|27  |William Ka wang Ma    |132              |William Ka wang Ma    |992   |Yancong Li            |973   |Allan Crawford        |992   |Allan Crawford        |992   |William Ka wang Ma    |585   |Kelsey Liang          |575   |Yancong Li            |980   |
|28  |Kelsey Liang          |132              |Angus Li              |985   |Sahil Rajesh Aggarwal |970   |William Ka wang Ma    |992   |William Ka wang Ma    |992   |Robert Stephen Foster |583   |Laurence Kao          |573   |Sahil Rajesh Aggarwal |978   |
|29  |John Ou               |132              |Andrew Meijer         |977   |Ratnesh Rao Ippili    |967   |Angus Li              |985   |Andrew Meijer         |977   |Kelsey Liang          |575   |John Ou               |573   |John Ou               |977   |
|30  |Angus Li              |132              |Laurence Kao          |956   |Robert Stephen Foster |967   |Laurence Kao          |957   |Laurence Kao          |956   |Yancong Li            |575   |Maurice Li            |571   |Robert Stephen Foster |970   |
|31  |Sarabpreet Singh Sodhi|132              |Arseny Shestakov      |956   |Laurence Kao          |956   |Arseny Shestakov      |956   |Arseny Shestakov      |956   |Laurence Kao          |573   |Colt Love             |546   |Laurence Kao          |957   |
|32  |Allan Crawford        |132              |Aakar Chatha          |954   |Aakar Chatha          |956   |Aakar Chatha          |954   |Aakar Chatha          |954   |Maurice Li            |571   |Andrew Meijer         |542   |Aakar Chatha          |956   |
|33  |Maurice Li            |132              |Dayton Se             |950   |Oliver Long           |955   |Dayton Se             |950   |Dayton Se             |950   |Ayush Ayush           |559   |Robert Stephen Foster |530   |Oliver Long           |955   |
|34  |Nicholas Poon         |49               |Oliver Long           |947   |Dayton Se             |950   |Oliver Long           |947   |Oliver Long           |947   |John Ou               |524   |Brendon Kwan          |523   |Roy Hung              |954   |
|35  |Justin Lam            |49               |Zhengheng Bao         |942   |Arseny Shestakov      |949   |Zhengheng Bao         |942   |Zhengheng Bao         |942   |Colt Love             |521   |Ayden Travis Lee      |519   |Dayton Se             |950   |
|36  |Oliver Long           |49               |Sahil Rajesh Aggarwal |936   |Zhengheng Bao         |949   |Sahil Rajesh Aggarwal |942   |Sahil Rajesh Aggarwal |936   |Oliver Long           |509   |Yancong Li            |519   |Arseny Shestakov      |949   |
|37  |Ayden Travis Lee      |49               |John Ou               |935   |Andy Le               |944   |John Ou               |935   |John Ou               |935   |Arseny Shestakov      |497   |Oliver Long           |511   |Zhengheng Bao         |949   |
|38  |Marcus James Tseng    |49               |Roy Hung              |912   |Bangjian (James) Geng |944   |Colt Love             |921   |Roy Hung              |915   |Aakar Chatha          |490   |Samuel Ha             |509   |Andy Le               |944   |
|39  |Aakar Chatha          |49               |Colt Love             |911   |Renjie Xiong          |938   |Roy Hung              |914   |Colt Love             |911   |Marcus James Tseng    |487   |Marcus James Tseng    |508   |Bangjian (James) Geng |944   |
|40  |Andy Le               |49               |Renjie Xiong          |907   |Yichen Li             |938   |Renjie Xiong          |907   |Renjie Xiong          |907   |Zhengheng Bao         |487   |Luca Ferretti         |497   |Ayush Ayush           |938   |
|41  |Arseny Shestakov      |49               |Justin Lam            |907   |Justin Lam            |937   |Justin Lam            |907   |Justin Lam            |907   |Brendon Kwan          |485   |Aakar Chatha          |490   |Renjie Xiong          |938   |
|42  |Hossein Ahmadi        |49               |Yichen Li             |907   |Hossein Ahmadi        |937   |Yichen Li             |907   |Yichen Li             |907   |Samuel Ha             |463   |Arseny Shestakov      |490   |Yichen Li             |938   |
|43  |Luca Ferretti         |49               |Andy Le               |905   |Luca Ferretti         |937   |Andy Le               |905   |Andy Le               |905   |Luca Ferretti         |460   |Zhengheng Bao         |487   |Justin Lam            |937   |
|44  |Robert Stephen Foster |49               |Bangjian (James) Geng |905   |Dwayne Da Silva       |937   |Bangjian (James) Geng |905   |Bangjian (James) Geng |905   |Dayton Se             |459   |Andy Le               |484   |Hossein Ahmadi        |937   |
|45  |Dwayne Da Silva       |49               |Hossein Ahmadi        |901   |Marcus James Tseng    |937   |Hossein Ahmadi        |901   |Hossein Ahmadi        |901   |Renjie Xiong          |456   |Renjie Xiong          |481   |Luca Ferretti         |937   |
|46  |Renjie Xiong          |49               |Luca Ferretti         |901   |Roy Hung              |936   |Luca Ferretti         |901   |Luca Ferretti         |901   |Dwayne Da Silva       |447   |Bangjian (James) Geng |478   |Dwayne Da Silva       |937   |
|47  |Zhengheng Bao         |49               |Dwayne Da Silva       |901   |Ayush Ayush           |936   |Dwayne Da Silva       |901   |Dwayne Da Silva       |901   |Andy Le               |446   |Dwayne Da Silva       |476   |Marcus James Tseng    |937   |
|48  |Yichen Li             |49               |Marcus James Tseng    |900   |Colt Love             |919   |Marcus James Tseng    |900   |Marcus James Tseng    |900   |Yichen Li             |444   |Hossein Ahmadi        |473   |Andrew Meijer         |924   |
|49  |Yancong Li            |49               |Ayush Ayush           |896   |Andrew Meijer         |919   |Ayush Ayush           |899   |Ayush Ayush           |896   |Bangjian (James) Geng |440   |Yichen Li             |469   |Colt Love             |923   |
|50  |Bangjian (James) Geng |49               |Samuel Ha             |850   |Brendon Kwan          |890   |Samuel Ha             |850   |Samuel Ha             |850   |Justin Lam            |437   |Justin Lam            |468   |Brendon Kwan          |892   |
|51  |Dayton Se             |0                |Brendon Kwan          |843   |Samuel Ha             |887   |Brendon Kwan          |846   |Brendon Kwan          |844   |Hossein Ahmadi        |436   |Dayton Se             |459   |Samuel Ha             |887   |

### Conclusion
In conclusion, with a few reasonable modifications to the ELO rating system to accomodate the Badminton BC consolation bracket, it is easy to create a player ranking based on match data that is more accurate than the official rankings based on tournament placement. Intuition proves correct, because with a Single Elimination Bracket, tournament placement does not describe winning ability as clearly as match results do. The next steps when revisiting this project are to develop the Advanced Variation, and then work on scaling up the amount of match input data. Saving tournament data to CSV files will have to be a manual process, but with Python it should be simple to add all of the tournaments as input files, so I don't need to change the code for each tournament I need to process (as I've been doing so far with only 2 tournaments). The essence of this project is complete, because the ranking in outputVariation6.csv is more accurate than officialRankings.csv, don't you agree? Regardless, there is a lot more that can still be done to improve the results.

### Author
Andrew Meijer
andrew@atrm.ca
