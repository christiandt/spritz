from spritz import Spritz

spritz = Spritz()
N = int(raw_input("N: "))
message = str(raw_input("Input: "))
r = int(raw_input("r: "))

hashed = spritz.hash(N, message, r)

print hashed