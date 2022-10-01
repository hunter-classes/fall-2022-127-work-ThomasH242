#4 and 6

def average(n):
    num = 0
    for i in n: # goes to the next int of the list
        num += i# 'i' gets the number from the list and adds it to num
    return num/len(n) # divide by size of list
test = [1,2,5,5,5]
print(average(test))

def sum_of_squares(xs):
    num = 0
    for i in xs:# goes to the next int of the list
        num += i**2 # i^2 adds to num
    return num
print(sum_of_squares(test))