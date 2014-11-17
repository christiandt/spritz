from re import findall
import matplotlib.pyplot as plt
import pickle, csv


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

def get_prns(key, length):
	ksa(key)
	numbers = []
	for i in range(length):
		numbers.append(prg())
	return numbers

def generate_data_file(key, length):
	numbers = get_prns(key, length)
	cnt = 0
	test = "   "
	with open('random.rc4', 'wb') as f:
		writer = csv.writer(f)
		for number in numbers:
			test += "{0:08b}".format(number)
			cnt += 1
			if cnt >= 3:
				print test
				writer.writerow([test])
				test = "   "
				cnt = 0
		writer.writerow([test])
		print test



print generate_data_file("spritz", 9000)