from spritz import Spritz
import matplotlib.pyplot as plt
import pickle


s = Spritz()

def get_binary():
	bit = int(round(s.drip()/225.0))
	return str(bit)

def generate_data_file(key, length):
	key = s.int_string(key)
	s.key_setup(key)
	i = 0.0
	with open('random.spritz', 'wb') as f:
		f.write(get_binary())
		i += 1.0
	while i <= length:
		with open('random.spritz', 'a+b') as f:
			f.write(get_binary())
			i += 1.0



generate_data_file("spritz", 512000000.0)