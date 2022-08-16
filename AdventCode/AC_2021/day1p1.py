# see problem description: https://adventofcode.com/2021/day/1
# See README for possible additional comments. - Andrew Meijer
# I don't think I need regex for this one

# variables
prev = 0 # previous number
ninc = 0 # number of increases (as per problem description)
input1 = open("input1.txt", "r")

# input first line as starting point
prev = int(input1.readline())

# for each additional line. . .
for curr in input1.readlines():
    # compare new line with previous line
    if int(curr) - prev > 0:
        # if the new line is larger value than previous line, add one to the total
        ninc = ninc + 1
    # update prev
    prev = int(curr)

# Close the file
input1.close()
# return the total.
print(ninc)