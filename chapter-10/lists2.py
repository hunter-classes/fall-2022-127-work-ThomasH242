#4 and 6

def average(n):
    num = 0
    for i in len(n):
        num = n.pop(i)
    return num/len(n)
test = [1,2,3,4,5]
average(test)