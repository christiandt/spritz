import unittest
from spritz import Spritz

class TestSpritz(unittest.TestCase):
    def setUp(self):
        self.s = Spritz()

    def test_hash(self):
        result = [hex(i) for i in self.s.hash(256, self.s.int_array("ABC"), 32)]
        self.assertEqual(result[0:8], ['0x2', '0x8f', '0xa2', '0xb4', '0x8b', '0x93', '0x4a', '0x18'])
        result = [hex(i) for i in self.s.hash(256, self.s.int_array("spam"), 32)]
        self.assertEqual(result[0:8], ['0xac', '0xbb', '0xa0', '0x81', '0x3f', '0x30', '0xd', '0x3a'])
        result = [hex(i) for i in self.s.hash(256, self.s.int_array("arcfour"), 32)]
        self.assertEqual(result[0:8], ['0xff', '0x8c', '0xf2', '0x68', '0x9', '0x4c', '0x87', '0xb9'])

    def test_encryption(self):
        result = [hex(i) for i in self.s.encrypt(self.s.int_array("ABC"), [0]*8)]
        self.assertEqual(result, ['0x77', '0x9a', '0x8e', '0x1', '0xf9', '0xe9', '0xcb', '0xc0'])
        result = [hex(i) for i in self.s.encrypt(self.s.int_array("spam"), [0]*8)]
        self.assertEqual(result, ['0xf0', '0x60', '0x9a', '0x1d', '0xf1', '0x43', '0xce', '0xbf'])
        result = [hex(i) for i in self.s.encrypt(self.s.int_array("arcfour"), [0]*8)]
        self.assertEqual(result, ['0x1a', '0xfa', '0x8b', '0x5e', '0xe3', '0x37', '0xdb', '0xc7'])


if __name__ == '__main__':
    unittest.main()