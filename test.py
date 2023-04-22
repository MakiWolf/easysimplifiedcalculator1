import unittest
 
from calculator import calculation_class
 
class Test_calulator(unittest.TestCase):
    def test_add(self):
        erg = calculation_class.add(5, 4)
        self.assertEqual(erg, 9.0)

    def test_sub(self):
        erg = calculation_class.sub(5, 4)
        self.assertEqual(erg, 1.0)

    def test_mult(self):
        erg = calculation_class.mult(5, 4)
        self.assertEqual(erg, 20.0)

    def test_div(self):
        erg = calculation_class.div(5, 5)
        self.assertEqual(erg, 1.0)
        

