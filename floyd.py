from spritz import Spritz
import sys

spritz = Spritz()
N = 256
r = 3
messages = ["banana", "apple", "message", "mouse", "spritz"]

def print_status():
    global counter
    counter+=1
    sys.stdout.flush()
    sys.stdout.write("Hashed: %i \r" % counter)
    return

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
            print_status()

def floyd():
    tortoise = torstart
    hare = harestart

    while tortoise != hare:
        tortoise = next(tortoise)
        hare = next(next(hare))
    print ""
    print "Cycle found at " + spritz.int_to_hex(hare)
    mu = 0
    tortoise = x0

    while tortoise != hare:
        tortoise = next(tortoise)
        hare = next(hare)
        mu += 1

    print "Cycle started after " + str(mu) + " hashes"
    return mu

print " *** %i bit *** " % (r*8)
for message in messages:
    print "Message: " + message
    message = spritz.int_string(message)
    hashlist = dict()
    x0 = spritz.hash(N, message, r)
    previous = spritz.hash(N, message, r)
    torstart = spritz.hash(N, previous, r)
    harestart = spritz.hash(N, torstart, r)
    counter = 0
    floyd()
