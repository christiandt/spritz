from spritz import Spritz
import random, pickle

spritz = Spritz()
N = 256
r = 3
#message = str(random.randint(0,256))
storage = open('list.pkl', 'wb')
hashlist = []

for i in range(10000):
	message = str(i)
	hashed = spritz.hash(N, message, r)
	hashlist.append(hashed)

print hashlist
pickle.dump(hashlist, storage)