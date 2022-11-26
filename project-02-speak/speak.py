#extras 
#store transitions in files Y
#punct, lower, and upper case Y
#translate different language X
#advanced translation Y
#---------------------------------------------------prep-----------------------------------------------------------------------
s = open('input.txt','r')#input
t = open("pirate.dat",'r')#pirate
sh = open("shakespeare.dat",'r')#shakespeare
ds = s.read().lower()#I
dt = t.read() #P
sha = sh.read()#S
nt = dt.split('\n')#P
shake = sha.split('\n')#S
punc = ['.',',',';','!','?']
#---------------------------------------------------convert list into dictionary-----------------------------------------------
def dictionary(dict):
    diction = {}
    for i in dict:#dict type is list, so i iterate through dict
        ph = i.find(':')# return number placement of colon
        i = i.lower()
        diction[i[0:ph]] = i[ph+1:99]#i[beginning : to the colon] = i [colon placement + 1(no colon) : end of i]
    return diction
#---------------------------------------------------uses dictionary in story---------------------------------------------------
def convert(story,dict):
    c = 0
    newstory = []
    placeholder = '' # - basically to add words into the new story
    previousi = ''
    for i in story.split(): #nested for loop
        c+=1
        checker = False # to check if the word is replaced already
        for j in dict.keys():
#this if statement is actually unreadable sorry
# if dict key == index of story "and" len of index with no punc == len of dict key
# if ^^^^^^^^^^^^^^^^^^^^^^^^^^ "and" len of index == len of dict key
# if previous index of story + " " + index of story in j
# if ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ index of story without punction in j
            if ((j in i and len(i)-1 == len(j)) or (j in i and len(i) == len(j)) or (previousi +" "+ i in j) or (previousi + " " + i[:-1] in j)):

                placeholder = dict.get(j).lower()
#same thing as line 37-38 but it pops out the word, because if key is 2 words it will leave the first word alone
                if((previousi +" "+ i in j) or (previousi + " " + i[:-1] in j)):
                    newstory.pop()
#if theres a . or first word or !, capitalize
                if(story.index(i) == 0 or '.' in previousi or '!' in previousi):
                    placeholder = placeholder.capitalize()
#if theres punc, add it
                if(any(k in i for k in punc)):
                    placeholder = placeholder + i[-1]
                checker = True
# if lines 39-51 did not happen then append the regular word
        if(checker == False): 
            if(story.index(i) == 0 or '.' in previousi or '!' in previousi):# capitalize
                newstory.append(i.capitalize())
            else:
                newstory.append(i)# --regular word--
        else:
            newstory.append(placeholder)# --dictionary word--
        previousi = i
    return '\n ' + " ".join(newstory)
#---------------------------------------------------audience input-------------------------------------------------------------
audience = ''
answer = ['pirate','shakespeare','exit']

while audience not in answer:
    audience = input("\n Hey! do you want to translate this to \n pirate \n shakespeare \n exit \n")
    if audience == 'pirate':
        print(convert(ds,dictionary(nt)))
    elif audience == 'shakespeare':
        print(convert(ds,dictionary(shake))) 
    elif audience == 'exit':
        exit()