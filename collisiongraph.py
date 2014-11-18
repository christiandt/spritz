import matplotlib.pyplot as plt
import numpy as np
import csv

r = []
collisions = []
total = 0
start_bit = 8
end_bit = 32
t1 = np.arange(0.0, 33.0, 0.1)

def expected(b):
	return np.sqrt(1-(2*np.log(0.5)*2**b))

with open('collision_test_test.csv', 'rb') as f:
	repetitions = 0
	prev_bit = start_bit
	reader = csv.reader(f)
	for row in reader:
		if row[0] == 'Bit': continue
		bit = int(row[0])
		message = row[1]
		hashes = int(row[2])
		cycle_after = int(row[3])
		cycle_node = row[4]
		if bit != prev_bit:
			r.append(prev_bit)
			collisions.append(total/repetitions)
			prev_bit = bit
			repetitions = 0
			total = 0
		total += hashes
		#total += cycle_after
		repetitions += 1
	r.append(prev_bit)
	collisions.append(total/repetitions)

print expected(32)
print r
print collisions
plt.plot(r, collisions, 'bo', t1, expected(t1), 'r')
plt.axis([0, 33, 0, 80000])
plt.title('Hash Collisions')
plt.xlabel('bits')
plt.ylabel('hashes')
plt.show()