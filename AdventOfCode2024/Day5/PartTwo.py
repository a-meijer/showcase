# Advent of Code 2024
# Day 5: Print Queue
# https://adventofcode.com/2024/day/5
# Andrew Meijer

'''
Find all the pages that are in the incorrect order according to the inputted rules,
Order them according to the rules,
Return a sum of middle page numbers.

My strategy here is to create a list of page objects, setting the status of each one to either correct or incorrect.
Create a sublist of all the incorrect entries.
Order them all.
Calculate the answer.
'''
     
# Return the sum of the middle page numbers
ans = 0

# File contents listed by row
contents = []
# Input the file contents
with open('input.txt', 'r') as file:
    for row in file:
        contents.append(row)

# Ordering rules list of tuples
rules = []
# intercessary input list
contents2 = []
# list of pages
pages = []
# list of incorrect pages
selectedPages = []

# FILE INPUT
# Use enumerate to get element indicies
for i, line in enumerate(contents):
    # if we get a blank line, we have reached the end of the ordering rules
    if(line == '\n'):
        # parse the contents into pages
        contents2 = contents[i+1:]
        break
    # Parse the page ordering rules as list of tuples
    try:
        num1, num2 = map(int, line.split('|'))
        rules.append(tuple([num1,num2]))
    except ValueError:
        print(line.split('|'), "Error", line)
    except TypeError:
        print("Type Error")
   
# Create a list of pages
for r in contents2:
    pages.append(list(map(int, r.split(','))))

# Inner part of the loop to iterate for each page, to determine correctness.
def selectIncorrectPages(p):
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
                    # add it to the list of rule-breakers
                    selectedPages.append(p)
                    return       
        # add the current element to the list of preceding elements before iterating
        prec.append(n)    

# For each set of pages
for p in pages:
    # Proceed to the inner loop
    selectIncorrectPages(p)

# When the loop completes, we should have a list of incorrect pages.
# Now it needs to be sorted according to the page ordering rules.
# For this, I can run through the pages and swap all the elements that break the rules
def swap(p, i, j):
    temp = p[i]
    p[i] = p[j]
    p[j] = temp
    return p

# Check if a rule is broken for a given page. Swap the elements at the first discovered break and return True. Otherwise, return False.
def check(p):
    # Nested loop to proceed for each pair x,y where p[x] precedes p[y] in p
    for x in range(len(p)):
        for y in range(x+1, len(p)):
            print("start loop:", p[x], p[y])
            for r in rules:
                # If the position of the numbers violates the rule
                if(r[0] == p[y] and r[1] == p[x]):
                    print("preswap", p)
                    p = swap(p,x,y)
                    print("postswap", p)
                    return True
    return False

# for each page
for p in selectedPages:
    # if the page breaks the rule, numbers will have been swapped
    # Repeat until no breaks are found
    counting = 0
    while(check(p) and counting < 10000):
        counting += 1


def middle(p):
    return p[int(len(p)/2)]

# Sum the totals of the middle numbers
for p in selectedPages:
    print(p)
    ans += middle(p)

# 4598
print(ans)