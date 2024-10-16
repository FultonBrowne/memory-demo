i = 0
def badidea():
    global i
    r = []
    i+=1
    r.append(i)
    badidea()
badidea()