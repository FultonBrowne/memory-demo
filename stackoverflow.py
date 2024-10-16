i = 0
r = []
def badidea():
    global i
    global r
    i+=1
    r.append(i)
    badidea()
badidea()