from spritz import Spritz


s = Spritz()

def get_binary():
	bits = "{0:08b}".format(s.drip())
	return bits

def generate_data_file(key, length):
	key = s.int_string(key)
	s.key_setup(key)
	numbers = ""
	for i in range(length):
		numbers += get_binary()
	with open('random.spritz.med', 'wb') as f:
		f.write(numbers)



generate_data_file("spritz", 1000000)