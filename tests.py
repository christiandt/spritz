import unittest
from spritz import Spritz

class TestSpritz(unittest.TestCase):
	def setUp(self):
		self.s = Spritz()

	def test_hash(self):
		self.assertEqual(self.s.hash(256, "ABC", 32)[0:8], ['0x02', '0x8f', '0xa2', '0xb4', '0x8b', '0x93', '0x4a', '0x18'])
		self.assertEqual(self.s.hash(256, "spam", 32)[0:8], ['0xac', '0xbb', '0x0a', '0x81', '0x3f', '0x30', '0x0d', '0x3a'])
		self.assertEqual(self.s.hash(256, "arcfour", 32)[0:8], ['0xff', '0x8c', '0xf2', '0x68', '0x09', '0x4c', '0x87', '0xb9'])


if __name__ == '__main__':
    unittest.main()