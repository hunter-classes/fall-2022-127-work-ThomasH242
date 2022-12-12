''' 
For example, one of the data sets in one of the above sits has Jeopardy questions. 
You could do a text analysis (Bag of Words) on Jeopardy questions. 
Another example would be taking pieces of 311 data and correlating them with each other or 
with some other data set. Like seeing if there’s a correlation between trash complaints and 
noise complaints with respect to zip code or some other type of complaint with crime data.
You should use the Python csv module to read in the data. You can look at the sample code we 
wrote but there are also lots of tutorials online.
If you want to show your analysis with plots and/or graphs, 
look up the Python mathplotlib library.
'''
import pandas as p
import matplotlib.pyplot as plot
import numpy as np
csv = p.read_csv('NYPDArrestList.csv')
def plotrace(race):
    fig = plot.figure(figsize = (10,10))
    plot.bar(list(race.keys()), list(race.values()), color = 'blue', width = 1)
    plot.xlabel("Races")
    plot.ylabel("People")
    plot.title(" People Arrested ")
    plot.show()

#Race---------------------------------------------------------------------------------------------------------------#
races = {'BLACK' : 0, 'WHITE' : 0, 'BLACK HISPANIC' : 0, 'WHITE HISPANIC' : 0, 'ASIAN / PACIFIC ISLANDER' : 0, 'AMERICAN INDIAN/ALASKAN NATIVE': 0, 'UNKNOWN': 0,}
for i in csv["PERP_RACE"]:
        races[i] +=1
newdict = {}
c = 0
for j in races:
    newdict[j[0:-3]] = races[j]
print(races)
#Gender---------------------------------------------------------------------------------------------------------------#
genders = {'M': 0, 'F' : 0}
for k in csv["PERP_SEX"]:
    genders[k]+= 1
perf = (genders['F']/genders['M'])*100
perm = (100-perf)
print("Males Percentage: ", perm)
print("Females Percentage: ",perf)
print("Genders", genders)
#plot---------------------------------------------------------------------------------------------------------------#
plotrace(races)