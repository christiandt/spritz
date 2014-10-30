from spritz import Spritz
from timeit import timeit

s = Spritz()

def keysize():
	print "%i bit key" % ((len(key)/3)*8)

def timingtest():
	s.key_setup(key)


key = s.int_string("keykeyke")
keysize()
for i in range(5):
	print timeit("timingtest()", setup="from __main__ import timingtest", number=100000)

key = s.int_string("ekyekyek")
keysize()
for i in range(5):
	print timeit("timingtest()", setup="from __main__ import timingtest", number=100000)