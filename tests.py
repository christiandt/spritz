import unittest
from spritz import Spritz

class TestSpritz(unittest.TestCase):
    def setUp(self):
        self.s = Spritz()

    def test_hash(self):
        result = self.s.int_to_hex(self.s.hash(256, self.s.int_string("ABC"), 32))
        self.assertEqual(result[0:16], '028FA2B48B934A18')
        result = self.s.int_to_hex(self.s.hash(256, self.s.int_string("spam"), 32))
        self.assertEqual(result[0:16], 'ACBBA0813F300D3A')
        result = self.s.int_to_hex(self.s.hash(256, self.s.int_string("arcfour"), 32))
        self.assertEqual(result[0:16], 'FF8CF268094C87B9')

    def test_encryption(self):
        result = self.s.array_to_string(self.s.encrypt(self.s.int_string("ABC"), [0]*8))
        self.assertEqual(result, '779A8E01F9E9CBC0')
        result = self.s.array_to_string(self.s.encrypt(self.s.int_string("spam"), [0]*8))
        self.assertEqual(result, 'F0609A1DF143CEBF')
        result = self.s.array_to_string(self.s.encrypt(self.s.int_string("arcfour"), [0]*8))
        self.assertEqual(result, '1AFA8B5EE337DBC7')

if __name__ == '__main__':
    unittest.main()