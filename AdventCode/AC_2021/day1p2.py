# see problem description: https://adventofcode.com/2021/day/1
# See README for possible additional comments. - Andrew Meijer

# variables
window1 = 0 # sum the first window of 3
window2 = 0 # sum the second window of 3
window3 = 0 # sum the third window of 3
windowFull1 = 0 # completed sum 1 (previous)
windowFull2 = 0 # completed sum 2
ninc = 0 # number of increases (output as per problem description)
input1 = open("input1.txt", "r") # input data stored in input1.txt

# input first line and add it to the first window
prev = int(input1.readline())

# input second line and add it to the first window; add it to the second window



# for each additional line. . .
for curr in input1.readlines():
    # add the line value to all 3 windows
    # window1 is now full; set windowFull2 to windowFull1 and set windowFull1 to window1

        # if the new line is larger value than previous line, add one to the total

    # update prev


# Close the file
input1.close()
# return the total.
print(ninc)