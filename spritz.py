import math
from fractions import gcd

class Spritz():

    def initialize_state(self, N_input):
        self.i = 0
        self.j = 0
        self.k = 0
        self.z = 0
        self.a = 0
        self.w = 1
        self.N = N_input
        self.D = int(math.ceil(math.sqrt(self.N)))
        self.S = range(self.N)

    def low(self, b):
        return b % self.D

    def high(self, b):
        return int(math.floor(b/self.D))

    def update(self):
        self.i = (self.i + self.w) % self.N
        self.j = (self.k + self.S[(self.j + self.S[self.i]) % self.N]) % self.N
        self.k = (self.i + self.k + self.S[self.j]) % self.N
        self.S[self.i], self.S[self.j] = self.S[self.j], self.S[self.i]

    def whip(self, r):
        for v in range(r):
            self.update()
        self.w = self.w + 1
        while gcd(self.w, self.N) != 1:
            self.w = (self.w + 1) % self.N

    def crush(self):
        for v in range(int(math.floor(self.N/2)-1)):
            if self.S[v] > self.S[self.N-1-v]:
                self.S[v], self.S[self.N-1-v] = self.S[self.N-1-v], self.S[v]

    def shuffle(self):
        self.whip(2*self.N)
        self.crush()
        self.whip(2*self.N)
        self.crush()
        self.whip(2*self.N)
        self.a = 0

    def absorb_nibble(self, x):
        if self.a == int(math.floor(self.N/2)):
            self.shuffle()
        self.S[self.a], self.S[int(math.floor(self.N/2)+x)] = self.S[int(math.floor(self.N/2)+x)], self.S[self.a]
        self.a += 1 % self.N

    def absorb_byte(self, b):
        self.absorb_nibble(self.low(b))
        self.absorb_nibble(self.high(b))

    def absorb(self, I):
        for v in I:
            self.absorb_byte(v)

    def absorb_stop(self):
        if self.a == int(math.floor(self.N/2)):
            self.shuffle()
        self.a += 1 % self.N

    def output(self):
        self.z = self.S[(self.j + self.S[(self.i + self.S[(self.z + self.k) % self.N]) % self.N]) % self.N]
        return self.z

    def drip(self):
        if self.a > 0:
            self.shuffle()
        self.update()
        return self.output()

    def squeeze(self, r):
        if self.a > 0:
            self.shuffle()
        P = []
        for v in range(r):
            P.append(self.drip())
        return P

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
#s.print_variables()      # test-print