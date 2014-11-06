import matplotlib.pyplot as plt
from spritz import Spritz
from timeit import timeit
from string_creator import String_Creator

s = Spritz()
string_maker = String_Creator()
values = dict()

def keysize():
	print "%i bit key" % ((len(key)/3)*8)

def timingtest():
	s.key_setup(key)


key = s.int_string("keykeyke")
#key = s.int_string(string_maker.create_string(8))
keysize()
for i in range(2000):
	time_result = round(timeit("timingtest()", setup="from __main__ import timingtest", number=100) * 1000, 2)
	#print time_result
	if time_result in values:
		values[time_result] += 1
	else:
		values[time_result] = 1


x_plot = []
y_plot = []
for value in values:
	x_plot.append(value)
	y_plot.append(values[value])

plt.bar(x_plot, y_plot, width=0.03)
plt.axis([6, 8, 0, 40])
plt.show()