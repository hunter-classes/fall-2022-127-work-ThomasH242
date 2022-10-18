# ctrl + /

#split filter 
import random
#opening and importing all the files  
mfile = open('sentence.txt', 'rt')
V = open('verbs.dat')
N = open('nouns.dat')
H = open('heroes.dat')
sentence = mfile.read()
vread = V.read()
nread = N.read()
hread = H.read()
vlist = vread.split()
nlist = nread.split()
hlist = hread.split()

#functions
def filters(S): 
    NS = S.split() #New Sentence
    c = 0 # int index
    for i in S.split():
#verb
        if i.lower() == '<verb>':
    # gets a random number from 0: length of verb list-1(it counts the size of the list STARTING at 1)
            ran = random.randint(0,len(vlist)-1) 
    # the new list[int index] = a verblist[random].lowercase()
            NS[c] = vlist[ran].lower()
    # If its the first word or the previous word had a period
            if(c == 0 or NS[c-1].find('.') > 0):
                NS[c] = vlist[ran].capitalize()
#noun
        elif i.lower() == '<noun>':
    # gets a random number from 0: length of noun list-1
            ran = random.randint(0,len(nlist)-1)
    # new list[int index] = a nounlist[random].lowercase()
            NS[c] = nlist[ran].lower()
    # first word or the previous word had a period
            if(c == 0 or NS[c-1].find('.') > 0):
                NS[c] = nlist[ran].capitalize()
#Hero 
        elif i.lower() == '<hero>':
    # random number from 0: length of hero list-1
            ran = random.randint(0,len(hlist)-1)
    # new list[int index] = a herolist[random]
            NS[c] = hlist[ran].capitalize()
        c+=1
    return " ".join(NS)            
    
print(filters(sentence))

# YO FIX CAPITALIZATION 