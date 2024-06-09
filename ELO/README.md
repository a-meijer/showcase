#ReadMe
##Purpose
The purpose of this project is to create a ranking system of the Men's Singles badminton players who participated in the 

##Introduction
The name of this project is ELO because even though it is used specifically on badminton data in this repository, the Elo Ranking System can be used with CSV files to easily create ranking systems for other competitive activities as well. This Readme will have 

###Creating CSV Files With Match Data
Matches are publicly available on badmintoncanada.tournamentsoftware.com
For the purposes of demonstration I will only use matches from two tournaments
Here is the link to the Men's Singles draw match page for the 2024 Jack Underhill:
https://badmintoncanada.tournamentsoftware.com/sport/drawmatches.aspx?id=6DBC438D-5F21-4544-9A89-C651CE550C1B&draw=11
Here is the link to the Men's Singles draw match page for the 2024 Provincial Championships:
https://badmintoncanada.tournamentsoftware.com/sport/drawmatches.aspx?id=5F17FF22-3C9F-4199-AE91-C0838750A59E&draw=22

This match data is publicly available; you can copy the match results into a spreadsheet, clean it down to two columns, and export the results to a CSV file.
Therefore, you can run this algorithm on matches from any other tournament on the badminton canada page.

###Creating the Python Files

###Tuning the Algorithm
####Choosing The K-Value
####Initial Ranking

###Results Analysis
####Comparing Elo Rankings to Official Rankings
####Clean Data
####Single Elimination With Consolation
####Double Elimination With Placement
It is necessary to switch to double elimination instead of single elimination with consolation in order for my ranking system to work better, because right now, consolation matches are weighted as heavily as main draw matches, and sorting the matches by whether or not they are main draw or consolation is easier said than done.

##Conclusion
If Badminton BC ran their tournaments with my Double-Elimination format instead of their Single-Elimination-With-Consolation format, the match data from those tournaments would produce a more accurate ranking through my algorithm.

##Author
Andrew Meijer