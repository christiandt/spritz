from spritz import Spritz


spritz = Spritz()
N = 256
r = 3
hashlist = dict()
message = "message"
message = spritz.int_string(message)

x0 = spritz.hash(N, message, r)
#print x0
previous = spritz.hash(N, message, r)
torstart = spritz.hash(N, previous, r)
harestart = spritz.hash(N, torstart, r)

def next(key):
    global previous
    while True:
        try:
            value = hashlist[key]
            return value
        except:
            current = spritz.hash(N, previous, r)
            hashlist[previous] = current
            previous = current

def floyd():
    tortoise = torstart
    hare = harestart

    while tortoise != hare:
        tortoise = next(tortoise)
        hare = next(next(hare))

    print "Cycle found at " + spritz.to_ascii_string(hare)
    mu = 0
    tortoise = x0

    while tortoise != hare:
        tortoise = next(tortoise)
        hare = next(hare)
        mu += 1

    print "Cycle started after " + str(mu) + " hashes"
    return mu

floyd()
