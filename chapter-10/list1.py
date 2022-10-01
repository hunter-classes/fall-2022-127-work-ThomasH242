from re import X


x = ["hello",True]

x.append("apple")
x.append(76)
x.insert(0,99)
print(x.index("hello"))
print(x.count(76))
print(x)
x.remove(76)
print(x)
x.pop(x.index(True))
print(x)