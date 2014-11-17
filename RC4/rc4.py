from re import findall

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

def encrypt(plaintext):
	ciphertext = ""
	for char in plaintext:
		ciphertext += '{0:02x}'.format(ord(char) ^ prg()).upper()
	return ciphertext

def decrypt(ciphertext):
	plaintext = ""
	for hex_num in findall('..', ciphertext):
		plaintext += chr(int(hex_num, 16) ^ prg())
	return plaintext


ksa('Key')
print prg()
print prg()
print prg()
print prg()
print prg()
print prg()

#ciph = encrypt('Plaintext')
#print ciph

#i = j = 0
#ksa('Key')
#plain = decrypt(ciph)
#print plain

#ksa('Wiki')
#ciph = encrypt('pedia')
#print ciph
#ksa('Wiki')
#plain = decrypt(ciph)
#print plain