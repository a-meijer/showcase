# Advent of Code 2024
# Day 3: Mull It Over
# https://adventofcode.com/2024/day/3#part2
# Andrew Meijer

'''
Part Two uses do() and don't() functions
to enable and disable the mul functions.
Using the regex or operator | makes this easy.
Once I have the clean input, I can enable and disable according to the dos and donts
'''

# import the regex library
import re

# Input the file contents
with open('input.txt', 'r') as file:
    contents = file.read().strip()

# initialize sum
ans = 0

# find all occurences of mul(X,Y), do(), and don't()
trim = re.findall(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)', contents)

# Use a boolean to track when we are doing
Do = True

# Use regex to find the numbers for each mul function
for i in trim:
    if(i == "do()"):
        Do = True

    elif(i == "don't()"):
        Do = False

    # all other elements are mul(X,Y)
    elif(Do): 
        nums = re.findall(r'\d+', i)
        ans += int(nums[0]) * int(nums[1])

# 165225049
print(ans)