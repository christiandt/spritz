import matplotlib.pyplot as plt

r = [1, 2, 3, 4, 5, 6]
collision = [12, 58, 169, 1871, 10576, 75908]

plt.bar(r, collision)
#plt.axis([0, 256, 0, 256])
plt.show()

prev = 0

for i in collision[::-1]:
    print prev/i
    prev = i