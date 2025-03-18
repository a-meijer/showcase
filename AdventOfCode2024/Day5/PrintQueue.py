# Advent of Code 2024
# Day 5: Print Queue
# https://adventofcode.com/2024/day/5
# Andrew Meijer

'''
Return a sum of middle page numbers:
Parse the input into the page ordering rules and the updates,
Determine which updates do not violate the page ordering rules,
Sum the middle numbers of each such update.
As I progress through the pages in each row of pages,
the plan is to generate lists of numbers that came before,
then for each element in this list, 
I can compare with the current element according to the rules.
'''

# Output the number of occurrences of XMAS in the graph
ans = 0

# File contents listed by row
contents = []
# Input the file contents
with open('input.txt', 'r') as file:
    for row in file:
        contents.append(row)

# Ordering rules list of tuples
rules = []
# intercessary list
pages = []
# list of pages
nums = []

# Use enumerate to get element indicies
for i, line in enumerate(contents):
    # if we get a blank line, we have reached the end of the ordering rules
    if(line == '\n'):
        # parse the contents into pages
        pages = contents[i+1:]
        break
    # Parse the page ordering rules as list of tuples
    try:
        num1, num2 = map(int, line.split('|'))
        rules.append(tuple([num1,num2]))
    except ValueError:
        print(line.split('|'), "Error", line)
    except TypeError:
        print("Type Error")
   
# pages still needs to be parsed into a list of lists called nums
for r in pages:
    nums.append(list(map(int, r.split(','))))

# Now rules and nums are parsed and ready for operations
print(rules)
print(nums)

# Use two lists to avoid ValueError exceptions when removing elements during the algorithm
pages = []
for i in nums:
    pages.append(i)

# for each set of pages
for p in nums:
    # Initialize the list of numbers that come before the current page
    prec = []
    # for each page
    for n in p:
        # for each number preceding the current page
        for m in prec:
            # for each page ordering rule
            for r in rules:
                # if a rule is broken
                if(r[0]==n and r[1]== m):
                    # remove the page
                    try:
                        pages.remove(p)
                    except ValueError:
                        # This exception runs a lot in the final solution, but it still outputs the correct answer
                        # Very ugly.
                        # I want to just skip to the next element n in p when I get to this line, after removing the page,
                        # But if I put a "continue" in here, it would continue out of the nested loop only.
                        # What I should've done is put this all in a function and returned to the parent loop. That's what I'll do in part 2
                        print("I want to continue in the parent loop")
                    
        # add the current element to the list of preceding elements before iterating
        prec.append(n)    

# When the loop completes, we should have a list of correct pages.
for p in pages:
    print(p)
    print(p[int(len(p)/2)])
    ans += p[int(len(p)/2)]

# 5452
print(ans)