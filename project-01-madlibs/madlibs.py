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
print(vlist,hlist,nlist)

#functions
def filters(S): 
    NS = S.split() #New Sentence
    c = 0 # int index
    v = ''
    n = ''
    for i in S.split():
#verb
        if i.lower() == '<verb>':
            ran = random.randint(0,len(vlist)-1)
            NS[c] = vlist[ran].lower()
            # If its the first word
            if(c == 0 or NS[c-1].find('.') > 0):
                NS[c] = vlist[ran].capitalize()
                print("lets go")
#noun
        elif i.lower() == '<noun>':
            ran = random.randint(0,len(nlist)-1)
            NS[c] = nlist[ran].lower()
            #if its the first word 
            if(c == 0 or NS[c-1].find('.') > 0):
                NS[c] = nlist[ran].capitalize()
#Hero 
        elif i.lower() == '<hero>':
            ran = random.randint(0,len(hlist)-1)
            NS[c] = hlist[ran].capitalize()
        c+=1
    return " ".join(NS)            
    
print(filters(sentence))

# YO FIX CAPITALIZATION 