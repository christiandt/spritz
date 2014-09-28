import math
from fractions import gcd

class Spritz():

    def initialize_state(self, N_input):
        self.i = 0  # i=j=k=z=a=0
        self.j = 0
        self.k = 0
        self.z = 0
        self.a = 0
        self.w = 1  # w=1
        self.N = N_input
        self.D = int(math.ceil(math.sqrt(self.N)))
        self.S = range(self.N)  #S[v] = v

    def low(self, b):
        return b % self.D   # b mod D

    def high(self, b):
        return int(math.floor(b/self.D))    # ⌊b/D⌋

    def update(self):
        self.i = (self.i + self.w) % self.N     # i=i+w
        self.j = (self.k + self.S[(self.j + self.S[self.i]) % self.N]) % self.N     # j=k+S[j+S[i]]
        self.k = (self.i + self.k + self.S[self.j]) % self.N    # k=i+k+S[j]
        self.S[self.i], self.S[self.j] = self.S[self.j], self.S[self.i]     # Swap(S[i], S[j])

    def whip(self, r):
        for v in range(r):  # for v=0 to r−1
            self.update()   # Update()
        self.w = self.w + 1 # do w=w+1
        while gcd(self.w, self.N) != 1: # until gcd(w,N) = 1
            self.w = (self.w + 1) % self.N

    def crush(self):
        for v in range(int(math.floor(self.N/2)-1)):    # for v=0 to ⌊N/2⌋−1
            if self.S[v] > self.S[self.N-1-v]:  # if S[v]>S[N−1−v]
                self.S[v], self.S[self.N-1-v] = self.S[self.N-1-v], self.S[v]   # Swap(S[v], S[N−1−v])

    def shuffle(self):
        self.whip(2*self.N) # Whip(2N)
        self.crush()        # Crush()
        self.whip(2*self.N) # Whip(2N)
        self.crush()        # Crush()
        self.whip(2*self.N) # Whip(2N)
        self.a = 0          # a=0

    def absorb_nibble(self, x):
        if self.a == int(math.floor(self.N/2)):     # if a=⌊N/2⌋
            self.shuffle()  # Shuffle()
        self.S[self.a], self.S[int(math.floor(self.N/2)+x)] = self.S[int(math.floor(self.N/2)+x)], self.S[self.a]   # Swap(S[a],S[⌊N/2⌋+x])
        self.a += 1 % self.N    # a=a+1

    def absorb_byte(self, b):
        self.absorb_nibble(self.low(b))     # AbsorbNibble(low(b))
        self.absorb_nibble(self.high(b))    # AbsorbNibble(high(b))

    def absorb(self, I):
        for v in I:     # for v=0 to I.length−1
            self.absorb_byte(v)     # AbsorbByte(I[v])

    def absorb_stop(self):
        if self.a == int(math.floor(self.N/2)):     # if a=⌊N/2⌋
            self.shuffle()  # Shuffle()
        self.a += 1 % self.N    # a=a+1

    def output(self):
        self.z = self.S[(self.j + self.S[(self.i + self.S[(self.z + self.k) % self.N]) % self.N]) % self.N]     # z = S[j+S[i+S[z+k]]]
        return self.z   # return z

    def drip(self):
        if self.a > 0:  # if a>0
            self.shuffle() # Shuffle()
        self.update()   # Update()
        return self.output()    # return Output()

    def squeeze(self, r):
        if self.a > 0:  # if a>0
            self.shuffle()  # Shuffle()
        P = []  # P = Array.New(r)
        for v in range(r):  # for v=0 to r−1
            P.append(self.drip())   # P[v] = Drip()
        return P    # return P

    def print_variables(self):
        print "i: " + hex(self.i)
        print "j: " + hex(self.j)
        print "k: " + hex(self.k)
        print "z: " + hex(self.z)
        print "a: " + hex(self.a)
        print "w: " + hex(self.w)
        print "S: " + str(self.S)

    def hash(self, N, M, r):
        self.initialize_state(N)
        self.absorb(M)
        self.absorb_stop()
        self.absorb_byte(r)
        return self.squeeze(r)

    def key_setup(self, K):
        self.initialize_state(256)
        self.absorb(K)

    def encrypt(self, K, M):
        self.key_setup(K)
        Z = self.squeeze(len(M))
        C = [i + j for i, j in zip(M, Z)]
        return C

    def int_array(self, string):
        key = []
        for char in string:
            key.append(int(char.encode("hex")))
        return key


#s = Spritz()
#print s.hash(256, "ABC", 32)
#s.print_variables()