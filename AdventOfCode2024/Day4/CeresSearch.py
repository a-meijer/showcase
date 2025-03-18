# Advent of Code 2024
# Day 4: Ceres Search
# https://adventofcode.com/2024/day/4
# Andrew Meijer

'''
Word search!
Write a program to solve word search puzzles.
First answer: 1245 too low! 
I made an error in my initial attempt where I was only counting
one word for each starting letter,
but it's possible that two "XMAS" occur with the same "X"
To correct this, instead of returning True from searchXMAS,
I return a number of occurrences.
Second answer: 2600 too high!
Now I am more stuck, because I get the correct answer on the sample data.
I need guidance from the internet.
This is adjacency matrix problem.
Instead of using a hard-coded function that looks for "XMAS"
I am going to build every 4-character string and check if it's "XMAS" afterwards.
Third time's the charm: 2532
'''
# Output the number of occurrences of XMAS in the graph
ans = 0

# Input the file contents
with open('input.txt', 'r') as file:
    contents = file.read().strip()

# use a function to search for the word XMAS wherever you find an X.
# where row and i index the location of the letter X to search from.
def searchXMAS(g, row, char):
    # 8 directions to search for the letter "MAS"
    # this is hard-coded but it is simple to search for a variable word 

    # Count the number of occurences per 'X'
    count = 0

    #search North
    #don't go out of bounds
    if(row-3 >= 0):
        if(g[row-1][char]=='M' and g[row-2][char]=='A' and g[row-3][char]=='S'):
            count += 1

    #search NorthEast
    if(row-3 >= 0 and char+3 < len(g[row])):
        if(g[row-1][char+1]=='M' and g[row-2][char+2]=='A' and g[row-3][char+3]=='S'):
            count += 1
    
    #search East
    if(char+3 < len(g[row])):
        if(g[row][char+1]=='M' and g[row][char+2]=='A' and g[row][char+3]=='S'):
            count += 1

    #search SouthEast
    if(row+3 < len(g) and char+3 < len(g[row])):
        if(g[row+1][char+1]=='M' and g[row+2][char+2]=='A' and g[row+3][char+3]=='S'):
            count += 1

    #search South
    if(row+3 < len(g)):
        if(g[row+1][char]=='M' and g[row+2][char]=='A' and g[row+3][char]=='S'):
            count += 1

    #search SouthWest
    if(row+3 < len(g) and char-3 >= 0):
        if(g[row-1][char-1]=='M' and g[row-2][char-2]=='A' and g[row-3][char-3]=='S'):
            count += 1

    #search West
    if(char-3 >= 0):
        if(g[row][char-1]=='M' and g[row][char-2]=='A' and g[row][char-3]=='S'):
            count += 1

    #search NorthWest
    if(row-3 >= 0 and char-3 >= 0):
        if(g[row-1][char-1]=='M' and g[row-2][char-2]=='A' and g[row-3][char-3]=='S'):
            count += 1

    return count


# Consider a 2D array to store the input data
# In Python this is a list of lists. Call it g for graph
g = []

# Create the list of lists of chars from file contents
g = [list(line) for line in contents.split("\n")]
n,m = len(g),len(g[0])

# set an 8-directional set of tuples for incrementing
adj8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]

for i in range(n):
    for j in range(m):
        # proceed in each of the 8 directions
        for dx,dy in adj8:
            # initialize cx,cy
            cx,cy = i,j
            # build up result as a 4-character string
            result = ""
            # loop 4 times to build a 4-character string
            for _ in range(4):
                # break if out of bounds
                if(cx not in range(n) or cy not in range(m)):
                    break
                # add to the result
                result += g[cx][cy]
                # increment the position in the matrix
                cx += dx
                cy += dy
            if result == "XMAS":
                ans += 1
# 2532
print(ans)