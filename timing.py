import matplotlib.pyplot as plt
from spritz import Spritz
from timeit import timeit
from string_creator import String_Creator

s = Spritz()
string_maker = String_Creator()
key = ""
runs = 1000

def keysize():
	print "%i bit key" % ((len(key)/3)*8)

def timingtest():
	s.key_setup(key)

def generate_data(alt):
	global key
	values = dict()
	s.alt = alt
	key = s.int_string("keykeyke")
	#key = s.int_string(string_maker.create_string(8))
	keysize()
	for i in range(runs):
		time_result = round(timeit("timingtest()", setup="from __main__ import timingtest", number=100) * 1000, 2)
		#print time_result
		if time_result in values:
			values[time_result] += (1.0/runs)
		else:
			values[time_result] = (1.0/runs)


	x_plot = []
	y_plot = []
	for value in sorted(values):
		x_plot.append(value)
		y_plot.append(values[value])
	return x_plot, y_plot

x_alt, y_alt = generate_data(True)
x_data, y_data = generate_data(False)

plt.plot(x_data, y_data, 'b', label='Original')
plt.plot(x_alt, y_alt, 'r', label='Prevent')
plt.legend(loc='upper right')
plt.axis([4.7, 5.2, 0, 0.13])
plt.title('Timing')
plt.xlabel('ms')
plt.ylabel('percent')
plt.show()