from spritz import Spritz
import random, pickle

spritz = Spritz()
N = 256
r = 1
storage = open('collisions.pkl', 'wb')

hashlist = []
collisions = []
counter = 0

while True:
	while True:
		message = spritz.hash(N, str(counter), r)
		if message in hashlist:
			out_text = "Collision at index: " + str(counter) + " and " + str(hashlist.index(message))
			print out_text
			collisions.append(out_text)
			pickle.dump(collisions, storage)
			break
		hashlist.append(message)
		counter += 1
	r += 1