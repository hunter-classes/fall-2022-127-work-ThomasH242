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
def ran(rand):
        return random.randint(0,len(rand)-1)
def filters(S): 
    NS = S.split() #New Sentence
    print(NS)
    c = 0 # int index
    # outside the for loop so the name wont change
    for i in S.split():
#verb
        if i.lower() == '<verb>':
    # the new sentence[int index] = a verblist[random].lowercase()
            NS[c] = vlist[ran(vlist)].lower()
    # If its the first word or previous word had period
            if(c == 0 or NS[c-1].find('.') > 0):
                NS[c] = vlist[ran(vlist)].capitalize()
#noun
        elif i.lower() == '<noun>':
            # gets a random number from 0: length of noun list-1
            #ran = random.randint(0,len(nlist)-1)
    # the new sentence[int index] = a nounlist[random].lowercase()
            NS[c] = nlist[ran(nlist)].lower()
    #if its the first word or previous word had period
            if(c == 0 or NS[c-1].find('.') > 0):
                NS[c] = nlist[ran(nlist)].capitalize()
#Hero 
        elif i.lower() == '<hero>':
    # Hero name wont change 
            NS[c] = hlist[ran(hlist)].capitalize()
        c+=1
    return " ".join(NS)          
    
print(filters(sentence))