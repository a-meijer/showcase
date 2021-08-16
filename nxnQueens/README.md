# Backtracking Recursion Readme
## Project Description
The purpose of this project is to compare backtracking algorithms that solve the NxN Queens problem. 
One algorithm will be written in C with structs, and another algorithm will be written in C++ with classes.

## nxn Queens, Backtracking Algorithms, and CSP
Backtracking algorithms are used to solve Constraint Satisfaction Problems (CSP), and NxN Queens is a CSP. For a problem to be CSP, it can be written as the problem of assigning variables to domains according to a set of constrains. In NxN Queeens, the problem is to put N Queens on an NxN chess board such that no Queens are attacking each other according to the rules of chess. In this project I will find all solutions for NxN Queens. With respect to CSP, the variables are the Queens, the domains are the squares on the board, and the constraint is that no Queen can be placed in attacking range of any other. To simplify the interface for this problem, the value N will be hardcoded into the source files, and the output to the console will be the total number of solutions. I will be solving NxN Queens as an enumeration problem, then testing for increasing values of N and recording the results. See the activity log for progress: INDEV entries are for drafting, ALPHA entries are for unit testing, BETA entries are for the comparison in the project description, and VERSION entries are for after the project is finished.
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

### C Solution with Datastructures
nxnQueens.c
The input variable n, for nxn queens is hard-coded into the source file, #define N 8, for example. 
To compile the source file enter in src directory,
    "gcc nxnQueens.c -Wall -o ../bin/cQueens"
To run the program,
    "../bin/cQueens"

### C++ Solution with Classes
nxnQueens.cpp
The input variable n, for nxn queens is hard-coded into the source file, #define N 8, for example. Therefore, no command-line arguments are needed.
To compile the source file in src directory,
    "g++ nxnQueens.cpp -Wall -o ../bin/cppQueens"
To run the program,
    "../bin/cppQueens"
