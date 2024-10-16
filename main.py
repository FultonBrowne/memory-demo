def getEvens(l):
    y = []
    for i in l:
        if i % 2 == 0:
            y.append(i)
    return y

def getOdds(l):
    y = []
    for i in l:
        if i % 2 != 0:
            y.append(i)
    return y


print("hello")

r = []
for i in range(100000):
    r.append(i)
reverselist = r.copy()
reverselist.reverse()
odds = getOdds(r)
evens = getEvens(r)
print("created")
input()
print(r)
print(odds)
print(evens)


