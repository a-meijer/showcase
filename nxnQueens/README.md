# Backtracking Recursion Readme
## Project Description
The purpose of this project was originally to compare backtracking algorithms that solve the NxN Queens problem. 
One algorithm was to be written in C a simple hard-coded enumeration solution, and another algorithm was to be written in C++ with classes.
Due to an obstructive unsolved bug in the cpp implementation, I decided to simplify this project just to measure the running time for different values of N in my C solution. I have left the C++ files in this project for future reference and I also have working linkedList samples which are interesting in relation to the bug. For more information about the bug, see Sample1 of my Bugs project in this same repository.

## nxn Queens, Backtracking Algorithms, and CSP
Backtracking algorithms are used to solve Constraint Satisfaction Problems (CSP), and NxN Queens is a CSP. For a problem to be CSP, it can be written as the problem of assigning variables to domains according to a set of constrains. In NxN Queeens, the problem is to put N Queens on an NxN chess board such that no Queens are attacking each other according to the rules of chess. In this project I will find all solutions for NxN Queens (with low values of N). With respect to CSP, the variables are the Queens, the domains are the squares on the board, and the constraint is that no Queen can be placed in attacking range of any other. To simplify the interface for this problem, the value N is hard-coded into the source file. I will be solving NxN Queens as an enumeration problem, then testing for increasing values of N and recording the results. The results are included in this readme file. See the activity log for progress notes: INDEV entries are for drafting, ALPHA entries are for unit testing, BETA entries are for the comparison in the project description, and VERSION entries are for after the project is finished.

## Results
Note: results may vary depending on the system running. I did get some variation in the clock values when running the executable multiple times. In future, to remedy this I will run many automated trials and take an avarage clock time. The results stop at N=15 because at that size it runs for several minutes. I could keep this running overnight and add more results later on. I think the WR for highest order is 27. The Wikipedia page for Eight Queens Puzzle has results for higher values of N, available here: https://en.wikipedia.org/wiki/Eight_queens_puzzle#Existence_of_solutions.
| N  | enumeration | clock  |
|----|-------------|--------|
| 1  | 1           | 0      |
| 2  | 0           | 0      |
| 3  | 0           | 0      |
| 4  | 2           | 0      |
| 5  | 10          | 1      |
| 6  | 4           | 0      |
| 7  | 40          | 1      |
| 8  | 92          | 1      |
| 9  | 352         | 10     |
| 10 | 724         | 54     |
| 11 | 2680        | 322    |
| 12 | 14200       | 2102   |
| 13 | 73712       | 14330  |
| 14 | 365596      | 101551 |
| 15 | 2279184     | 783914 |

### Activity Log
activityLog.txt is filled with numbered entries that record progress in the completion of this project. INDEV entries are for drafting, ALPHA entries are for unit testing, BETA entries are for the comparison in the project description, and VERSION entries are for after the project is finished.

## Source Files
To compile source files, using the Command Prompt or Terminal enter the "src" directory. . . (for this project, I used VS Code on Windows 10)
### Linked List in C
linkedList.c is included just for reference when building other source files.
The number of nodes in the list and the integer data values for each node are hardcoded into the source file.
To compile the source file enter,
    "gcc linkedList.c -Wall -o ../bin/cLinkedList"
To run the program enter,
    "../bin/cLinkedList"

### Linked List in Cpp
linkedList.cpp is included just for reference when building other source files.
The number of nodes in the list and the integer data values for each node are hardcoded into the source file.
To compile the source file,
    "g++ linkedList.cpp -Wall -o ../bin/cppLinkedList"
To run the program,
    "../bin/cppLinkedList"

### C Solution with 2D char array
nxnQueens.c
The input variable n, for nxn queens is hard-coded into the source file, #define N 8, for example. 
To compile the source file enter in src directory,
    "gcc nxnQueens.c -Wall -o ../bin/cQueens"
To run the program,
    "../bin/cQueens"

### C++ Solution with Classes and Vectors
nxnQueens.cpp
This file is buggy. Ignore it. For more information see Bugs project, Sample1.
