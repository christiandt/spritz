from spritz import Spritz
import matplotlib.pyplot as plt
import pickle, csv


s = Spritz()


def get_prns(key, length):
	key = s.int_string(key)
	s.key_setup(key)
	numbers = []
	for i in range(length):
		numbers.append(s.drip())
	return numbers

def generate_data_file(key, length):
	numbers = get_prns(key, length)
	cnt = 0
	test = "   "
	with open('random.spritz', 'wb') as f:
		writer = csv.writer(f)
		for number in numbers:
			test += "{0:08b}".format(number)
			cnt += 1
			if cnt >= 3:
				print test
				writer.writerow([test])
				test = "   "
				cnt = 0
		writer.writerow([test])
		print test



print generate_data_file("spritz", 100000)