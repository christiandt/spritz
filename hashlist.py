from spritz import Spritz
import random, pickle

spritz = Spritz()
N = 256
r = 3
#message = str(random.randint(0,256))
storage = open('list.pkl', 'wb')
hashlist = []
message = spritz.hash(N, "message", r)

for i in range(10000):
	if(message) in hashlist: 
		print "duplicate i: "+str(i)+" prev: "+str(hashlist.index(message))
		break
	res = spritz.hash(N, message, r)
	hashlist.append(message)
	message = res

print hashlist
pickle.dump(hashlist, storage)
storage.close()