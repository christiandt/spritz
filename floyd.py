from spritz import Spritz
from string_creator import String_Creator
import sys, csv

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
            #print_status()

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
    return mu, spritz.int_to_hex(hare),


spritz = Spritz()
string_generator = String_Creator()

# N_values = [64, 128, 256]
N_values = [256]
r_values = [1, 2, 3, 4]

with open('collision_test_test.csv', 'w') as f:
    writer = csv.writer(f)
    #writer.writerow(["N", "Bit", "Message", "Hashes", "Cycle pos", "Cycle Node"])
    writer.writerow(["Bit", "Message", "Hashes", "Cycle pos", "Cycle Node"])
    for N in N_values:
        for r in r_values:
            messages = string_generator.random_list(2, 6)

            print " *** %i bit *** " % (r*8)
            for message_string in messages:
                print "Message: " + message_string
                message = spritz.int_string(message_string)
                hashlist = dict()
                x0 = spritz.hash(N, message, r)
                previous = spritz.hash(N, message, r)
                torstart = spritz.hash(N, previous, r)
                harestart = spritz.hash(N, torstart, r)
                counter = 0
                cycle_start, cycle_value = floyd()
                # row = [N, (r*8), message_string, counter, cycle_start, cycle_value]
                row = [(r*8), message_string, counter, cycle_start, cycle_value]
                writer.writerow(row)
