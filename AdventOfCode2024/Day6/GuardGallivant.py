# Advent of Code 2024
# Day 6: Guard Gallivant
# https://adventofcode.com/2024/day6
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


# Parse the input into a char map
g = [list(line) for line in contents.split("\n")]
n,m = len(g),len(g[0])

for x in g:
    print(x)