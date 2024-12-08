# Advent of Code 2024
# Day 3: Mull It Over
# https://adventofcode.com/2024/day/3
# Andrew Meijer

'''
This is a regex problem.
Thankfully, python makes regex easy!
I just have to look up the syntax.

I first submitted my answer to this problem using \d{3} instead of \d+
but that wasn't big enough. It says in the problem description that the numbers
are at most 3 characters.
I realized, \d{3} only returns 3-digit numbers, not at-most 3-digit numbers!
'''

# import the regex library
import re

# Input the file contents
with open('input.txt', 'r') as file:
    contents = file.read().strip()

# initialize sum
ans = 0

# find all occurences of mul(X,Y)
# where X and Y are AT MOST 3-digit numbers.
# "mul" matches mul
# "\(" matches (
# "," matches ,
# "\d{3}" matches 3-digit numbers
# "\)" matches )
trim = re.findall(r'mul\(\d+,\d+\)', contents)

# Now with the trimmed input, we can use regex to find the numbers for each mul function
for i in trim:
    nums = re.findall(r'\d+', i)
    ans += int(nums[0]) * int(nums[1])

# 165225049
print(ans)