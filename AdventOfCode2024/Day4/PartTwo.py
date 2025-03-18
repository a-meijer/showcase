# Advent of Code 2024
# Day 4: Ceres Search
# https://adventofcode.com/2024/day/4#part2
# Andrew Meijer

'''
My understanding is that the MAS has to be an X but not a +
So the lines of the X have to be perpendicular.
There are a few different ways to interpret the problem as written.
'''

# Output the number of occurrences of XMAS in the graph
ans = 0

# Input the file contents
with open('input.txt', 'r') as file:
    contents = file.read().strip()


# Create the list of lists of chars from file contents
g = [list(line) for line in contents.split("\n")]
n,m = len(g),len(g[0])

# set an 8-directional set of tuples for searching
# adj8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
dirs1 = [(1,1),(1,-1),(-1,1),(-1,-1)]
dirs2 = [(1,0),(0,1),(-1,0),(0,-1)]

for i in range(n):
    for j in range(m):
        # count the number of MAS (TEST)
        MAStest = 0
        # search in each of the 8 directions
        for dx,dy in dirs1:
            # initialize cx,cy
            cx,cy = i,j
            # initialize result string
            result = ""
            
            # break if out of bounds
            if(cx+dx not in range(n) or cy+dy not in range(m) or cx-dx not in range(n) or cy-dy not in range(m)):
                break
            # add to the result
            result += g[cx+dx][cy+dy]
            result += g[cx][cy]
            result += g[cx-dx][cy-dy]
            
            if result == "MAS":
                MAStest += 1

            # If there is a X using dirs1, the result will be 2
            if(MAStest == 2):
                ans += 1
                # And I think we're gonna reset
                MAStest = 0

# 2614 is TOO HIGH
# 2610 not tested
# 1895 not tested
# 1941 is correct
print(ans)