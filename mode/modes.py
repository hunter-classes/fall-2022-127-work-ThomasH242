
def findLargest(l):
    max = l[0]
    for i in l:
        if i > max:
            max = i
    return max

def freq(l,v):
    c = 0
    for i in l:
        if i == v:
            c+=1
    return c

list = (4,2,1,5,8,4,4,1,7,2,6)
print(findLargest(list), "find largest")
print("there are ",freq(list,4), "of the same numbers")