from re import findall
import matplotlib.pyplot as plt
import pickle, sys


S = []
i = 0
j = 0

def ksa(keystring):
	global S
	key = []
	S = []

	for char in keystring:
		key.append(ord(char))

	for i in range(256):
		S.append(i)

	j = 0
	for i in range(256):
		j = (j + S[i] + key[i % len(key)]) % 256
		S[i], S[j] = S[j], S[i]


def prg():
	global S, i, j

	i = (i + 1) % 256
	j = (j + S[i]) % 256
	S[i], S[j] = S[j], S[i]
	z = S[(S[i] + S[j]) % 256]
	return z

def get_binary():
	bit = int(round(prg()/225.0))
	return str(bit)

def generate_data_file(key, length):
	ksa(key)
	numbers = ""
	for i in range(length):
		sys.stdout.flush()
		sys.stdout.write("Generating: %i \r" % i)
		numbers += get_binary()
	with open('random.rc4', 'wb') as f:
		f.write(numbers)


generate_data_file("spritz", 512000000)