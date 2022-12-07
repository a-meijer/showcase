# README Advent of Code
## Project Description
Hello.
I am currently working on Advent of Code 2021, starting on December 6, 2021.
I am using python for Advent of Code 2021 because I think leveraging regex with help me input data from files easily
Based on what I discovered from Advent of Code 2020, problems require file i/o.
I am hoping that regex will save a lot of time with this project.

## Activity Log
### Day 1 : Part 1
Consider this section of the README as a reference point for progress in this project.
December 6, 2021: I am starting on Day 1 of Advent of Code 2021.
Created file day1p1.py
Created file input1.txt
Puzzle input for day X is to be stored in inputX.txt where X is a day of the advent of code.
Okay, I put comments in the ticket. It is simple file I/O and I got through some errors by adding integer parsing and using readlines()
Output 1999. . . Wrong answer.
It's because I haven't been updating prev. Updated.
Output 1477. . . Correct!
### Day 1 : Part 2
December 7, 2021:
Created file day1p2.py
Now we are measuring differently, but using the same data.
I think it is possible that regex could help me here. Searching online: https://docs.python.org/3/library/re.html
also, https://docs.python.org/3/howto/regex.html#regex-howto
On second thought, I am not so sure regex can help me with this one. I just need to read the lines in groups of 3.
I don't want to be redundant though. Let's sort it out without regex.
After the first two measurements, every measurement needs to be read into 3 different measurement-windows.