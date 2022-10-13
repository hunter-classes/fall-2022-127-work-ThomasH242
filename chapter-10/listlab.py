from tkinter import E
from unicodedata import east_asian_width
import math
#Write a function to find the smallest value in a listKfind smallest in a list of items
def small(smoll):
    mini = smoll[0]#MINI GETS FIRST ITEM OF LIST 
    for i in smoll:
        if i < mini:# IF INDEX IS LESS THAN MINI, THAN MINI WILL EQUAL INDEX 
            mini = i
    return mini
#Write a function that returns a new list that contains all the odd items in the original list
def odd(olist):
    newlist = []
    for i in olist: 
        if(i % 2 == 1): # IF I HAS REMAINDER THAN APPEND I TO NEWLIST
            newlist.append(i)
    return newlist

#Write a function that takes a string and returns a new string where all the words are capitalized.
def Capitalized(olist):
   newlist = ''
   for i in olist.split():
        newlist += i.capitalize() + " " # CAPITALIZE EACH WORD AND ADD IT TO NEWLIST
   return newlist

#Write a function that takes a string and returns a new string with every word that's longer than 5 character turned into upper case
def upfive(olist):
    newlist = []
    for i in olist.split():# SPLIT EACH WORDS BY THE SPACES AND ADDED TO A LIST
        if len(i) > 4: # IF ITS GREATER THAN 4 CHARACTERS UPPERCASE ALL THE CHARACTERS FROM THE WORD
            i = i.upper()
        newlist.append(i)
        sentence = " ".join(newlist)
    return sentence

#Write a function that takes a list of numbers and returns a new list with each item squared
def sqr(olist): 
    newlist = [] 
    placeholder = 0
    for i in olist: 
        placeholder = i**2 #I^2
        newlist.append(placeholder)#NEWLIST APPEND I^2
    return newlist
""" Write a function that takes two lists of numbers and returns a new list where each item is the corresponding 
    values of the original lists added together. Ex [1,2,3] and [10,20,30] would return the list [11,22,33]      """
def twolist(l1,l2):
    newlist = []
    for index in range(0,len(l1),1):# THIS STARTS FROM THE 0 PLACEMENT TO THE LENGTH OF LIST 1
        newlist.append(l1[index]+l2[index]) # NEWLIST APPENDS THE LIST 1 + LIST 2
    return newlist
#10 
def count(list):
    c=0
    for i in list:
        if len(i) > 4: # IF LENGTH OF I IS GREATHER THAN 4 THAN C+1
            c +=1
    return c

#11
def sum(l):
    sum = 0
    i = 0
    while l[i] % 2 != 0 and i < len(l):# WHILE INDEX OF LIST MOD 2 = 0 AND INDEX IS LESS OF THE LENGTH OF THE LIST THAN SUM ADD INDEX 
        sum += l[i]
        i+=1
    return sum

#12
def sam(l):
    count = 0
    i = 0
    while l[i].lower() != 'sam' and i < len(l): #WHILE THE INDEX OF THE LIST IS NOT EQUAL TO SAM AND INDEX IS LESS THAN LIST
        count += 1
        i += 1
    return count + 1
#----------------------------------------------------------------------------------------------#
ex = [24454,23,3434,21]#1
print(small(ex)," #1")
exa = [1,2,3,4,5,6,7,8,9,10]#2
print(odd(exa)," #2")
e = ("hello my name is thomas and today is my birthday ")
ea = ("hello", "my ","name", "is" ,"thomas" ,"and" ,"today" ,"is" ,"my" ,"birthday")
sa = ("Hello", "my", "name", "is", "sam")
print(Capitalized(e)," #3")
print(upfive(e)," #4")
print(sqr(exa), " #5")
l1 = [2,6,90,2,1,2]
l2 = [5,1,78,4,1,3]
print(twolist(l1,l2), " #6")
print(count(ea)," #7")
print(sum(l2), " #8")
print(sam(sa))
#----------------------------------------------------------------------------------------------#