import matplotlib.pyplot as plt
import csv

r = []
collisions = []
total = 0
start_bit = 8
end_bit = 32

with open('collision_results_final.csv', 'rb') as f:
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
		#total += hashes
		total += cycle_after
		repetitions += 1
	r.append(prev_bit)
	collisions.append(total/repetitions)

print r
print collisions
plt.plot(r, collisions, 'bo-')
#plt.axis([0, 256, 0, 256])
plt.show()