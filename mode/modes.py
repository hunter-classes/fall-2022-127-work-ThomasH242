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
def buildRandomList(s,m):#size/max value
    l = []
    i = 0
    while i != s:
        l.append(random.randint(1,m))
        i+=1
    return l
    
def mode(l):
    msf = l[0]
    freqsf = freq(l,msf)
    for i in l:
        if freq(l,i) > freqsf:
            msf = i
            freqsf = freq(l,i)
    return msf
def fastMode(dataset):
    tallies = [0] * 100
    for i in dataset:
        tallies[i] +=1
    maxv = max(tallies)
    mode = tallies.index(maxv)
    #IF LIST HAS TWO MODES, IT RETURNS BOTH OF THE VALUES
    #_____________________
    #talliestwo = [0] * 100
    #datasettwo = [j for j in dataset if j != mode]
    #for k in datasettwo:
    #    talliestwo[k] +=1
    #maxvtwo = max(talliestwo)
    #modetwo = 0
    #if(maxvtwo == maxv):
    #    modetwo = talliestwo.index(maxvtwo)
    #    return mode, modetwo
    return mode
def testMode(s,max):
    l = buildRandomList(s,max)
    m = mode(l)
    print(m)
    return m
def testFindLargest(size,maxValue):
    print("Dataset Size: ",size)
    dataset = buildRandomList(size,maxValue)
    # print(dataset)
    m = findLargest(dataset)
    print("Largest: ",m)
list = buildRandomList(100,20)
#print(findLargest(list), "find largest")
#print("there are ",freq(list,4), "of the same numbers")
#print(mode(list))
#print(buildRandomList(10,20))
list.sort()
print(list)
print(fastMode(list))
