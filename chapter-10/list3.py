def max(list):
    m = 0
    for i in list:
        if i > m:
            m = i
    return m
l = [1,35,8,1,3,9,4874,2,2,1,9]
print(max(l),'max')
def odd(list):
    c = 0
    for i in list:
        if i % 2 == 1:
            c+= 1
    return c
print(odd(l), 'odd')
def even(list):
    c = 0
    for i in list:
        if i % 2 == 0:
            c+= i
    return c
print(even(l),'even')

'''def lenfive(list):
    c = 0
    for i in list:
        if len(i)== 5:
            c +=1
    return c
list = ["hello","where","are","you","my","godde"]
print(lenfive(list))'''