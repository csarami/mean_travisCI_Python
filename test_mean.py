import unittest
import mean

class MyTest(unittest.TestCase):
	def test_3(self):
		self.assertEqual(mean.mean([1,2,3]),2)
	def test_empty(self):
		self.assertEqual(mean.mean([]),0)

if __name__ == '__main__':
	unittest.main()
