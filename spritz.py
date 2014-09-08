import math
from fractions import gcd

S = []
D = 0
N = 0

def initialize_state(N_input):
    global S, D, N
    i = j = k = z = a = 0
    w = 1
    N = N_input
    D = int(math.ceil(math.sqrt(N)))
    S = range(N)

def low(b):
    return b % D

def high(b):
    return int(math.floor(b/D))

def update():
    global S, i, j, k
    i = i + w
    j = k + S[j+S[i]]
    k = i + k + S[j]
    S[i], S[j] = S[j], S[i]

def whip(r):
    for v in range(r):
        update()
    w = w + 1
    while gcd(w, N) != 1:
        w = w + 1

def crush():
    for v in range(math.floor(N/2)-1):
        if S[v] > S[N-1-v]:
            S[v], S[N-1-v] = S[N-1-v], S[v]

def shuffle():
    global a
    whip(2*N)
    crush()
    whip(2*N)
    crush()
    whip(2*N)
    a = 0

def absorb_nibble(x):
    global S, a
    if a = int(math.floor(N/2)):
        shuffle()
    S[a], S[math.floor(N/2)+x] = S[math.floor(N/2)+x], S[a]
    a = a + 1

def absorb_byte(b):
    absorb_nibble(low(b))
    absorb_nibble(high(b))

def absorb(I):
    for v in range(len(I)):
        absorb_byte(I[v])

def absorb_stop():
    if a = int(math.floor(N/2)):
        shuffle()
    a = a + 1

def output():
    z = S[j + S[i + S[z + k]]]
    return z

def drip():
    if a > 0:
        shuffle()
    update()
    return output()

def squeeze(r):
    pass


initialize_state(256)
print S
print D
print N

print low(50)
print high(50)