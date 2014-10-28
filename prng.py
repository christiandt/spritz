from spritz import Spritz
import matplotlib.pyplot as plt

s = Spritz()
points = 9000

def plot_prng(key):
	s.key_setup(s.int_array(key))
	numbers = []
	for i in range(points):
		numbers.append(s.drip())
	plt.plot(range(points), numbers, 'ro')
	plt.axis([0, points, 0, 256])
	plt.show()

plot_prng("spritz")