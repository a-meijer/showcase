# Bugs - Sample 1 
## Bug Description
This bug is in C++. I first experienced this bug when working with C on an N by N Queens project. After working around the bug for my the C files, I encountered the bug again for the C++ files, at which point I decided to create this Bugs project and cut C++ out of my N by N Queens project.
The nature of this bug is that testFile1.cpp doesn't print, but after commenting out a few lines, it does print, as shown in testFile2.cpp. Whether initializing classes or structs, it seems to cause this problem. When I run the executable, it hangs for a second before terminating.
The puzzle here is to solve why testFile1 does not print anything out, but testFile2 does print.
Note, there is a lot of extra code here aside from what's bugging, so my idea of the first steps in solving this are to remove the irrelevant parts. I might also consider recreating the bug in C with structs instead of classes. I suspect the issue is caused by having an object with a pointer to that same object inside, but it worked with linkedlists.cpp in my nxnQueens project.

## Compilation
Source files for this project are contained in the src subdirectory, and the executables are in the bin subdirectory.
Thus, get to src in your CLI first, or else your compilation instructions will be different.

### testFile1.cpp
To compile the source file enter,
    "g++ testFile1.cpp -Wall -o ../bin/file1"
To run the program enter,
    "../bin/file1"

### testFile1.cpp
To compile the source file enter,
    "g++ testFile2.cpp -Wall -o ../bin/file2"
To run the program enter,
    "../bin/file2"