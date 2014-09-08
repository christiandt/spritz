S = []
i = 0
j = 0

def ksa(keystring):
	global S
	key = []
	for char in keystring:
		key.append(ord(char))

	for i in range(256):
		S.append(i)

	j = 0
	for i in range(256):
		j = (j + S[i] + key[i % len(key)]) % 256
		S[i], S[j] = S[j], S[i]


def prg():
	global S
	global i
	global j

	i = i + 1
	j = j + S[i]
	S[i], S[j] = S[j], S[i]
	z = S[S[i] + S[j]]
	return z



ksa('Key')
print S
print prg()