from tkinter import E
from unicodedata import east_asian_width
import math
def small(s):
    num = s[0]
    for i in s:
        if i < num:
            num = i
    return num
def odd(l):
    nl = []
    for i in l:
        if(i % 2 == 1):
            nl.append(i)
    return nl
def C(l):
   e = ''
   for i in l.split():
        e += i.capitalize() + " "
   return e
def upfive(st):
    nl = []
    for i in st.split():
        if len(i) > 4:
            i = i.upper()
        nl.append(i)
        sentence = " ".join(nl)
    return sentence
def sqr(l):
    nl = [] 
    n = 0
    for i in l:  
        n = i**2
        nl.append(n)
    return nl
def twolist(l1,l2):
    nl = []
    for i in range(0,len(l1),1):
        nl.append(l1[i]+l2[i])
    return nl
def count(list):
    c=0
    for i in list:
        if len(i) > 4:
            c +=1
    return c
def sum(l):
    sum = 0
    i = 0
    while l[i] % 2 != 0 and i < len(l):
        sum += l[i]
        i+=1
    return sum
def sam(l):
    count = 0
    i = 0
    while l[i].lower() != 'sam' and i < len(l):
        count += 1
        i+=1
    return count+1
ex = [24454,23,3434,21]#1
print(small(ex)," #1")
exa = [1,2,3,4,5,6,7,8,9,10]#2
print(odd(exa)," #2")
e = ("hello my name is thomas and today is my birthday ")
ea = ("hello", "my ","name", "is" ,"thomas" ,"and" ,"today" ,"is" ,"my" ,"birthday")
sa = ("Hello", "my", "name", "is", "sam")
print(C(e)," #3")
print(upfive(e)," #4")
print(sqr(exa), " #5")
l1 = [2,6,90,2,1,2]
l2 = [5,1,78,4,1,3]
print(twolist(l1,l2), " #6")
print(count(ea)," #7")
print(sum(l2), " #8")
print(sam(sa))