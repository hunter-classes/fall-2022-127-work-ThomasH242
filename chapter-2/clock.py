cts = input("What is the current time (military) ")
wts= input("How many hours do you have to wait? ")
cti = int(cts)
wti = int(wts)
hours = cti + wti
timeofday = hours % 24
print(timeofday)