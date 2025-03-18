# Advent of Code 2024
# Day 2: Red-Nosed Reports Part 2
# https://adventofcode.com/2024/day/2#part2
# Andrew Meijer

'''
To add the dampener described in part two,
I can't simply skip an entry if it would cause the row to be unsafe
because my current algorithm detects ascending/descending based off the first 2 entries.
If I find that a row should be ascending because of the first two entries,
but the rest of the row is descending, that's still SAFE.
I think I need a different means of detecting ascending/descending.
I think the way I use loops is not ideal for python,
looping through the indexes like C instead of using "for each".

I am going to change the algorithm to detect ascending/descending based on the contents of the entire row
If the row would be unsafe because of an ascending/descending error, remove the error entry
My plan is to determine which entries are out of line, and if there is only one, to remove it.

There must be a simpler way. . .
I want to be able to check ascending/descending all in one go.
Maybe Python has some functionality for this.
I found a player Neil Thistlethwaite  who uses functions "any", "all", and "zip"
so I am looking those up to see what they do.
All returns true if all of the list inputs are true.
Zip creates a list of tuples. If one list is longer than the other, extra elements are removed.
Neil also uses list slices to remove the first element like this: row[1:]

In order to check this for the case where I need to remove an erroneous entry,
I will create a function to call, def check that returns true or false.
Then I can call the function and sum the true results.
To do this, I will first isolate my file input so I don't have the file open the whole time.

'''

# Input the file contents
with open('input.txt', 'r') as file:
    contents = file.read().strip()

def check(row):
    # Insight from Neil Thistlethwaite to determine truth of Ascending or Descending
    # make sure to get your parentheses right on this!
    SAFE = all(a > b for a,b in zip(row, row[1:])) or all(a < b for a,b in zip(row, row[1:]))

    if(SAFE):
        # use tuples and zip to easily compare elements
        for a,b in zip(row, row[1:]):
            # check if the row is unsafe
            if(abs(b-a) > 3 or abs(b-a) < 1):
                SAFE = False
                break
            
    return SAFE


#main

# Create empty lists to store each row of numbers
line = []

# Calculate the sum of the booleans for each row
SUM = 0

#create rows of integers from file contents
for line in contents.split("\n"):
    line = list(map(int, line.split()))

    # run the function for each row all variations of each row missing one element
    # lists can be appended with the + operator
    # row[:i] + row[i+1:] for i in range(len(row)) produces all rows with 1 element missing
    if(check(line)) or any(check(line[:i] + line[i+1:]) for i in range(len(line))):
        SUM += 1

# SUM = 601
print(SUM)