## ReadMe
### Purpose
To demonstrate a ranking system for badminton that is more accurate than the official rankings for British Columbia.

### Introduction
The official Badminton BC Senior Men's Singles Rankings are based on tournament results (placement) in only two tournaments:
 - 2024 Jack Underhill
 - 2024 Provincial Championships
These two tournaments determined the official Badminton BC Senior Men's Singles Badminton Rankings as of June 1, 2024: https://badmintoncanada.tournamentsoftware.com/ranking/category.aspx?id=39968&category=415
A ranking based on tournament placement alone is suboptimal because the luck of the draw creates inaccuracies in the rankings compared to what can be achieved with a ranking system based on match results, especially because tournament organizers use a Single Elimination format instead of Double Elimination. Double Elimination creates a more accurate placement result, a higher resolution result if you will. Plus, it makes the matches more meaningful because it doesn't require any consolation matches. Copying match data from tournaments on badmintoncanada.tournamentsoftware.com and creating a ranking system based on match results is another way to create a higher resolution ranking, especially with a large number of matches. The more data, the better.
The Elo Ranking System can be used with CSV files to easily create ranking systems for almost any competitive activity. 
The algorithm at work in this project uses two CSV files: 
 - inputRankings.csv
 - inputMatches.csv
It works by creating a dictionary of player objects based on the data in inputRankings.csv and then updating the dictionary based on the data in each line of inputMatches.csv. The algorithm then outputs the data to a hardcoded output CSV file. This is implemented in each of the Python files for each of the variations of the prototype.

### Creating CSV Files With Match Data
The first iteration of prototypes for this ELO ranking system run on only the data from the same tournaments that contribute to the 2024 rankings. This is to demonstrate how changes to the algorithm's initialization affect the results. Later iterations will include match results from additional tournaments.
Matches are publicly available on badmintoncanada.tournamentsoftware.com, but apparently it is against the site policy to use automation to scrape the website for data. It is easy enough to manually copy and paste the match results into spreadsheets.
In the first iteration of prototyping, the algorithm only uses matches from the two tournaments that were used to determine the current BC Senior Rankings as of June 1, 2024.

Here is the link to the Men's Singles draw match page for the 2024 Jack Underhill:

https://badmintoncanada.tournamentsoftware.com/sport/drawmatches.aspx?id=6DBC438D-5F21-4544-9A89-C651CE550C1B&draw=11

Here is the link to the Men's Singles draw match page for the 2024 Provincial Championships:

https://badmintoncanada.tournamentsoftware.com/sport/drawmatches.aspx?id=5F17FF22-3C9F-4199-AE91-C0838750A59E&draw=22

After getting the match data ready, I ran a test program to create a CSV containing the rankings and I confirmed there were no duplicates. Now, the test file no longer exists and I have a new CSV inputRankings.csv to initialize all of the ratings for all of the players that appear in inputMatches.csv in this sample data. To run the algorithm on larger data, I would need to rewrite the code to create inputRankings.csv while removing duplicates.
##### For this algorithm to work, inputRankings.csv has to already contain all the player names that appear in inputMatches.csv. This algorithm does not read in new players on the fly unlike the old version that I neglected to upload before losing.

### Understanding the Algorithm
#### Elo's Formulas
Arpad Elo was nice enough to publish the formulas for his Elo algorithm, and they are now available on Wikipedia. His algorithm requires two formulas.

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
I decided to create Player objects and point to them in a Python dictionary, indexed by player name. If two players have a match together, select their ratings from the rank dictionary, load in the match result to the S variable, select a K constant (if necessary), and then run the formulas! Formula 1 calculates the expected outcome (between 0 and 1) for each player and Formula 2 updates the rankings.
Repeat for each match in the dataset, and then output the new rankings when done.

#### Considering an Object Oriented Solution
Creating Player objects is something I went back and forth on during the development of this project. It would've been possible to do the algorithm with just a list of tuples. In the end I decided to go with Player objects because they are conceptually easy to work with and they're easily scaleable in case I want to add more features like match history or aliases.

### Creating the Initial Prototype Python File updateRankings.py
The name of the file to run on the CSV data is called updateRankings.py.
Use the following command:
``
python updateRankings.py
``
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
The initial prototype works according to the code snippet above and there are a few ways to change it meaningfully such as by choosing a different K-value or adapting the initial rankings, without reimplementing the entire algorithm. This will be demonstrated later in Variations.

#### Choosing The K-Value for Rating Sensitivity
The K value is set as a constant 100 in the initial prototype and it affects the amount of rating change after a single match. The algorithm could be improved by using a dynamic K-value that changes based on the recent match results of each player. This is demonstated later in Variations.

### Results Analysis
#### Comparing Initial Prototype updateRankings.py to Official Rankings
As expected, due to the extremely low number of matches for these ratings, consolation players get overrated and there are some unfortunate bad ratings. Considering the sample size of data, these initial results are decently accurate. The accuracy improves with more match data. Note that the BC rankings are based on points from tournament placement where as the Elo rankings are based on match results.

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

### Prototype Discussion
What would improve the accuracy of this prototype the most is addressing the problem of consolation champions being overranked. There are many ways to improve this algorithm. Notably, factoring-in tournament placement could make the system more approachable for people who are used to rankings that depend solely on tournament placement. Consider the variations below

### Variations
 - changing K value based on consolation (requires separating each tournament into its own CSV file; we know we are in consoles after our first loss)
 - Using function of tournament points as initial ranking
 - changing K value based on number of matches played
 - changing K value based on streakiness
 - changing K value based on number of games in the match - if you go three games or if you get to extra points, especially in the third, you don't lose as much ranking.
 - changing K value based on the tournament type (see Badminton BC page for how that works on tournament points)
 - combined variation

### Variations Compared to Official Rankings


### Conclusion
Work in progress

### Author
Andrew Meijer
andrew@atrm.ca
