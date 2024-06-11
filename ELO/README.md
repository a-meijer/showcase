## ReadMe
### Purpose
The purpose of this project is to create a ranking system of the Men's Singles badminton players who participated in the  2024 Jack Underhill and 2024 Provincial Championships, because these two tournaments determined the official Badminton BC Senior Men's Singles Badminton Rankings as of June 1, 2024: https://badmintoncanada.tournamentsoftware.com/ranking/category.aspx?id=39968&category=415
Unfortunately, Badminton BC's current ranking system is not very accurate, so I would advise Badminton BC to use my ranking system instead, running my algorithm on as many tournaments as possible, using match data from all of the tournaments on badmintoncanada.tournamentsoftware.com.

### Introduction
The Elo Ranking System can be used with CSV files to easily create ranking systems for almost any competitive activity. This project contains three main files: inputRankings.csv, inputMatches.csv, and updateRankings.py. updateRankings.py is used to create new rankings based on the input rankings and matches. When the algorithm is run on an empty or nonexistent inputRankings.csv file, a new one will be created according to the results of the matches.

### Creating CSV Files With Match Data
Matches are publicly available on badmintoncanada.tournamentsoftware.com
For the purposes of demonstration I will only use matches from the two tournaments that were used to determine the current BC Senior Rankings as of June 1, 2024.

Here is the link to the Men's Singles draw match page for the 2024 Jack Underhill:

https://badmintoncanada.tournamentsoftware.com/sport/drawmatches.aspx?id=6DBC438D-5F21-4544-9A89-C651CE550C1B&draw=11

Here is the link to the Men's Singles draw match page for the 2024 Provincial Championships:

https://badmintoncanada.tournamentsoftware.com/sport/drawmatches.aspx?id=5F17FF22-3C9F-4199-AE91-C0838750A59E&draw=22

This match data is publicly available! For this project, I copied the match results into a spreadsheet, clean it down to two columns, and export the results to a CSV file. Also make sure to CTRL + F, Replace All the various notes that go at the end of each player name for seeding.
Anyone can run this algorithm on matches from almost any other tournament with match data on tournament software. 

Be warned, it is against the site policy to use a computer program to scrape the website for data.

After getting the match data ready, I ran a test program to create a CSV containing the rankings and I confirmed there were no duplicates. Now, the test file no longer exists and I have a new CSV inputRankings.csv to initialize all of the ratings for all of the players that appear in inputMatches.csv in this sample data. To run the algorithm on larger data, I would need to rewrite the code to create inputRankings.csv while removing duplicates.
##### For this algorithm to work, inputRankings.csv has to already contain all the player names that appear in inputMatches.csv. This algorithm does not read in new players on the fly unlike the old version that I neglected to upload before losing.

### Understanding the Algorithm
#### Elo's Formulas
Arpad Elo was nice enough to publish the formulas for his Elo algorithm, and they are now available on Wikipedia. His algorithm requires two formulas.

Formula 1:
![FormulaImage](formula1.jpg)

``
EA = 1/(1 + 10^((RB-RA)/400))
``

Formula 2:
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
In Python, we can use the assignment operator to overwrite R_A with R'_A, and we can store all our variables in a neat and tidy data structure.
I think a Python dictionary works best as a data structure for this because I can index by player name and it's very intuitive to work with. If two players are going to have a match together, we select their ratings from the rank dictionary, load in the match result to the S variable, select a K constant (if necessary), and then run the formulas! Formula 1 calculates the expected outcome (between 0 and 1) for each player and Formula 2 updates the rankings.
Repeat for each match in the dataset, and then output the new rankings when done.

#### Considering an Object Oriented Solution
Creating Player objects is something I went back and forth on during the development of this project. It would've been possible to do the algorithm with just a list of tuples. In the end I decided to go with Player objects because they are conceptually easy to work with and they're easily scaleable in case I want to add more features like match history or aliases.

### Creating the Python File
ChatGPT greatly enhanced my productivity for this project by helping to answer questions about Python syntax. I created my Python file in VSCode and implemented the Elo algorithm.

The file runs from top to bottom of course, it imports the CSV library; declares filename variables; initializes the Player class, the rank dictionary, and the K-constant, all global variables; and creates a function that I later use to sort the rankings.

Once inside the body of the Python code, it opens the rankings CSV file. Now, I already have my CSV file pre-made, but if you need to make your own, as I mentioned earlier, it's a simple procedure of outputting a Set of names from the match CSV to a different CSV file. The rankings are loaded in as a Python dictionary indexed by player names, pointing to Player objects. I open the match data file and include the crux of the algorithm:

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

### Tuning the Algorithm
The algorithm works according to the code snippet above and there are a few ways to change it meaningfully such as choosing a different K-value or adapting the initial rankings, without reimplementing the entire algorithm.

#### Choosing The K-Value for Rating Sensitivity
The K value is set as a constant 100 in this algorithm and it represents the upper limit on rating change after a single match. The algorithm could be improved by using a dynamic K-value that changes based on the recent match results of each player, or changes based on the context of the match. For example, matches in provincial championships could have a higher K-value than matches in a regional tournament, matches in the semifinals could have a higher K-value than matches in the Round of 16, or matches in the main draw could have a higher K-value than matches in consolation. I think changing the K-value based on a player's entire match history is reasonable. Changing the K-value based on the number of games in a match is also possible. If a player wins by a large margin, their rating could reasonably go up more than if they won by a small margin.

#### Initial Ranking
initial ranking affects the algorithm greatly because my match data is so small. One way to correct this would be to have the initial rating of a winning player (if it is their first match) become the rating of their opponent until they win a match. This would require that I update the Player data structure to record match history. Another simpler way to correct this is to run the algorithm twice. After the first run the players get a better initial ranking, and after the second run the rankings are more accurate, arguably. It could be worth collecting match data from past tournaments to determine initial rankings for this algorithm. The order in which matches are passed through the algorithm affects the results. No matter the details of initial ranking, the best way to get accurate rankings is to run the algorithm through a lot of match data. 

### Results Analysis
As expected, due to the extremely low number of matches for these ratings, consolation players get overrated and there are some unfortunate bad ratings. Considering the sample size of data, these initial results are decently accurate. The accuracy improves with more match data.

#### Comparing Elo Rankings to Official Rankings
We can compare the rankings here. Note that the BC rankings are based on points from tournament placement where as the Elo rankings are based on match results.

| BC Rank | Player Name     | Points | Elo Rank | Player Name      | Rating |
|---------|-----------------|--------|----------|------------------|--------|
|      1  | Saurabh Pandiar |  1488  |       1  | Saurabh Pandiar  |  1356  |
|      2  | Simar Singh     |   935  |       2  | Nicholas Poon    |  1185  |
|      3  | Jalil Waiz      |   930  |       3  | Lyem Fedoretz    |  1173  |
|      4  | Jack Chen       |   810  |       4  | Ryan Liu         |  1134  |
|      5  | Connor Louie    |   805  |       5  | Simar Singh      |  1122  |
|      6  | Kwun Ho So      |   685  |       6  | Victor Ho        |  1119  |
|      7  | Lyem Fedoretz   |   533  |       7  | Anish Jojula     |  1085  |
|      8  | Uday Bharti     |   520  |       8  | Jalil Waiz       |  1084  |
|      9  | Sahil Aggarwal  |   509  |       9  | Jack Chen        |  1079  |
|      9  | Ratnesh Ippili  |   509  |      10  | Uday Bharti      |  1067  |
|     11  | Victor Ho       |   439  |      11  | Ayden Travis Lee |  1065  |
|     11  | Ryan Liu        |   439  |      12  | Jaden Thom       |  1061  |
|     13  | Roy Hung        |   400  |      12  | Kwun Ho So       |  1061  |
|     14  | Anish Jojula    |   345  |      14  | Connor Louie     |  1052  |
|     15  | Jaden Thom      |   307  |      15  | Kevin Wu         |  1043  |
|     15  | Ayush Ayush     |   307  |      16  | Rickey Zhang     |  1042  |
|     17  | Rickey Zhang    |   225  |      17  | Stephen Dee      |  1037  |
|     17  | Kevin Wu        |   225  |      18  | Ratnesh Ippili   |  1035  |
|     17  | Jasper Kong     |   225  |      19  | Yancong Li       |  1031  |
|     17  | Stephen Dee     |   225  |      20  | Jasper Kong      |  1025  |
|     21  | Colt Love       |   224  |      21  | Allan Crawford   |  1019  |
|     21  | Andrew Meijer   |   224  |      22  | Sarabpreet Sodhi |  1014  |
|     21  | Brendon Kwan    |   224  |      23  | Robert Shi       |  1007  |
|     21  | Samuel Ha       |   224  |      24  | Angus Li         |   993  |
|     25  | Laurence Kao    |   175  |      24  | Kelsey Liang     |   993  |
|---------|-----------------|--------|----------|------------------|--------|


### Discussion
Where can we take it from here? There are many ways to improve this algorithm. Notably, factoring-in tournament placement could make the system more approachable for people who are used to rankings that depend solely on tournament placement. 
For Elo rankings to work well, we need a good interplay between all of the strong players. If we tried adding rankings for the Women's Singles players, they would be effectively distinct from the Men's ratings unless the women interplayed with men. The effect of bad interplay appears in my results because of consolation bracket. In the match data, since the consolation bracket is distinct from the main draw, players who win lots of matches in consolation get an inflated rating until they are stopped by a main draw player at the next tournament. To this, I prefer a double elimination bracket formula for three main reasons. Double elimination creates more interplay because players from the main draw drop into the lower bracket every round, it creates more layering and meaningful matches for lower level players because they still have a chance to affect ranking and placement, and it removes the unlucky annoyance of getting eliminated to the top seed in the first or second round. With double elimination, there is still hope to win the entire tournament!

#### Single Elimination With Consolation
Most badminton tournaments in the province of BC and across Canada run a format called Single Elimination With Consolation. In this format, the tournament entrants compete in a single-elimination bracket, and the players who lose their first match are entered into a consolation bracket which is also single elimination. Bracket formats work on a base two system. Consider a tournament with 8, 16, 32, 64, or 128 entrants, and fill up the empty entries with Byes. If a player gets a Bye in their first round and they lose their match in the second round, they are eligible for consolation.

#### Double Elimination
It is necessary to switch to double elimination from single elimination for my ranking system to work better, because right now, consolation matches are weighted as heavily as main draw matches. Imagine a tournament format where your matches are just as meaningful after a loss! Imagine a tournament format where an unlucky draw won't ruin your event! All of this is possible and more with Double Elimination. I have already drawn up so many bracket designs for 8 to 16 players, I have a notebook full of designs! I've thought about this a lot, and I've even calculated the approximate costs for running a tournament. I think double elimination would be much more fun for the players and everyone involved overall.

### Conclusion
If Badminton BC ran their tournaments with my double elimination format instead of their single elimination with consolation format, the match data from those tournaments would produce a more accurate ranking through my algorithm because every match of a double elimination tournament is more meaningful than consolation. I won't use this conclusion to only sing the praises of double elimination because after all this is about my Python Elo system. It's not just about badminton, this ranking system works for other competition too. To update the rankings on new matches, simply copy the output rankings CSV back into the input and the rankings will grow in accuracy!
For anyone who wants to implement this on their own, one thing to be careful of is that you will need to adjust the code when adding new players, or you can add them manually in the ranks CSV. Make sure the names match. This system could be customized for different applications.
Thanks!

### Author
Andrew Meijer
andrew@atrm.ca
