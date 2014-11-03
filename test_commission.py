import unittest

from Commission import Commission

class TestCase(unittest.TestCase):

	def setUp(self):
		self.c = Commission()

	def test_ventas_1000_1000_1000(self):
		self.assertEqual(19860.0,self.c.calcular(1000,1000,1000))

	def test_ventas_4_0_0(self):
		self.assertEqual(18.0,self.c.calcular(4,0,0))

	def test_ventas_11_11_11(self):
		self.assertEqual(115.0,self.c.calcular(11,11,11))

if __name__ == '__main__':
	unittest.main()