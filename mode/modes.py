import random
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
def mode(l):
    msf = l[0]
    freqsf = freq(l,msf)
    for i in l:
        if freq(l,i) > freqsf:
            msf = i
            freqsf = freq(l,i)
    return msf

def buildRandomList(s,m):#size/max value
    l = []
    i = 0
    while i != s:
        l.append(random.randint(1,m))
        i+=1
    return l
def testMode(s,max):
    l = buildRandomList(s,max)
    m = mode(l)
    print(m)
    return m
list = (4,2,1,5,8,4,4,1,7,2,6,8,8,8)
print(findLargest(list), "find largest")
print("there are ",freq(list,4), "of the same numbers")
print(mode(list))
print(buildRandomList(10,20))
print(testMode(20,10))