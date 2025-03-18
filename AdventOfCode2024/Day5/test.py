p=[2,1,3,4,5]

rules=[(1,2),(2,3),(3,4),(4,5)]

def swap(p, i, j):
    temp = p[i]
    p[i] = p[j]
    p[j] = temp
    return p

def check(p):
    # Nested loop to proceed for each pair x,y where p[x] precedes p[y] in p
    for x in range(len(p)):
        for y in range(x+1, len(p)):

            for r in rules:
                # If the position of the numbers violates the rule
                if(r[0] == p[y] and r[1] == p[x]):
                    p = swap(p,x,y)
                    return True
            return False


x=0
booler = True
while(booler and x<100):
    booler = check(p)
    x+=1
    print(p)

