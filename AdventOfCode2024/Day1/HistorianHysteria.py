# Advent of Code 2024
# Day 1: Historian Hysteria
# https://adventofcode.com/2024/day/1
# Andrew Meijer

'''
Alright, it's time to get my homework done.
The first thing I have to do is sign up for Advent of Code 2024. I will do that with my Github account.
Step two I have to get my puzzle input. Clicking the link for the input displays the data. I Used CTRL + A to select it and copy it into a text file.
I pasted the data into a file in this directory called input.txt.
Quick shoutout to Aria AI for the file IO syntax, and I'm ready to input these numbers to solve the problem.
This file IO is great because it splits each line into two integers regardless of the delimiter.
'''

# Create empty lists to store the numbers
list1 = []
list2 = []

# Open the file for reading
with open('input.txt', 'r') as file:

    # Read each line in the file
    for line in file:
        # Split the line into two numbers
        num1, num2 = map(int, line.split())
        
        # Append the numbers to their respective lists
        list1.append(num1)
        list2.append(num2)

# Sort the lists
list1.sort()
list2.sort()

sum = 0

# For each pair, calculate the difference. Track the sum.
for x in range(0,len(list1)):
    sum += abs(list1[x] - list2[x])

# Final output 2086478
print(sum)

