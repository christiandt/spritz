import pickle

storage = open('list.pkl', 'rb')
hashlist = pickle.load(storage)
print "test"+str(len(hashlist))

def floyd():
    tortoise = 1
    hare = 2
    while hashlist[tortoise] != hashlist[hare]:
        tortoise += 1
        hare += 2
        if hare >= 2000: hare = 2
        if tortoise >= 2000: tortoise = 1
        print hare
        print tortoise
    mu = 0
    tortoise = 0
    while hashlist[tortoise] != hashlist[hare]:
        tortoise += 1
        hare += 1
        mu += 1
        if hare >= 2000: hare = 2
        if tortoise >= 2000: tortoise = 1
    return mu


print "mu: " + str(floyd())
