import math

S = []
D = 0
N = 0

def initialize_state(N_input):
	global S, D, N
	i = j = k = z = a = 0
	w = 1
	N = N_input
	D = int(math.ceil(math.sqrt(N)))
	for v in range(N):
		S.append(v)

def low(b):
	return b % D

def high(n):
	return int(math.floor(b/D))

def absorb_byte(b):
	absorb_nibble()

def absorb(I):
	for v in range(len(I)):
		absorb_byte(I[v])


initialize_state(256)
print S
print D
print N