from spritz import Spritz
import matplotlib.pyplot as plt
import pickle, csv


s = Spritz()

def get_binary():
	bit = int(round(s.drip()/225.0))
	return str(bit)

def generate_data_file(key, length):
	key = s.int_string(key)
	s.key_setup(key)
	numbers = ""
	for i in range(length):
		numbers += get_binary()
	with open('random.spritz', 'wb') as f:
		f.write(numbers)



generate_data_file("spritz", 10000000)