# Advent of Code 2024
# Day 2: Red-Nosed Reports
# https://adventofcode.com/2024/day/2
# Andrew Meijer

'''
Output a sum of 1s and 0s where,
SAFE rows produce a 1 and,
UNSAFE rows produce a 0.
Calculate the difference between adjacent numbers in the row.
If the difference is less than 1 or greater than 3, it's UNSAFE.
If the first number is larger than the second, set descending,
and all numbers must be descending or else it's UNSAFE.
If the first number is smaller than the second, set ascending,
and all numbers must be ascending or else it's UNSAFE.
If two adjacent numbers are equal, it's UNSAFE.
Otherwise it's safe.
'''

# Open the file for reading
with open('input.txt', 'r') as file:

    # Create empty lists to store each row of numbers
    row = []

    # Calculate the sum of the booleans for each row
    SUM = 0
    

    # Read each line in the file
    for line in file:
        # Parse the line into a list of numbers
        row = list(map(int, line.split()))
        
        # Initialize SAFE to 1, and set it to 0 if the line is unsafe
        SAFE = 1

        # Determine if the line should be ascending or descending
        if(row[1] - row[0] > 0):
            ASCENDING = 1
        else:
            ASCENDING = 0

        # Start the loop at 1 to index with i-1
        for i in range(1,len(row)):
            # Set unsafe if difference is too big or small
            if(abs(row[i]-row[i-1]) > 3 or abs(row[i]-row[i-1]) < 1):
                SAFE = 0
            
            # Set unsafe if numbers are equal
            if(row[i] == row[i-1]):
                SAFE = 0

            # Set unsafe if numbers are not all either ascending or descending
            if(ASCENDING == 1):
                if(row[i] - row[i-1] < 0):
                    SAFE = 0
            
            if(ASCENDING == 0):
                if(row[i] - row[i-1] > 0):
                    SAFE = 0

        SUM += SAFE

    # SUM = 559
    print(SUM)
