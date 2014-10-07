from spritz import Spritz
import random, pickle

spritz = Spritz()
N = 256
r = 3
#message = str(random.randint(0,256))
storage = open('list.pkl', 'wb')
hashlist = []

for i in range(2000):
	message = str(i)
	hashlist.append(spritz.hash(N, message, r))

print hashlist
pickle.dump(hashlist, storage)