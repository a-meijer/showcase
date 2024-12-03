# Advent of Code 2024
# Day 1: Historian Hysteria Part 2
# https://adventofcode.com/2024/day/1#part2
# Andrew Meijer

# Add up each number in the left list after multiplying it by the number of occurrences in the right list.

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

sum = 0
# for each element of the first list, multiply it by the number of occurences in the second list
for x in list1:
    # count the number of occurrences in the second list
    count = 0
    for y in list2:
        if y==x:
            count += 1

    # multiply by the number of occurences
    sum += x*count        

# sum = 24941624
print(sum)