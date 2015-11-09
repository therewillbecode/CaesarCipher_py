__author__ = 'Tom'
import unittest
import sys
# Add the ptdraft folder path to the sys.path list
sys.path.append('/Users/Tom/PycharmProjects/vector_class/Vector_Calc_py')

import index

obj = index.CaesarCipher(1)

obj2 = index.CaesarCipher(2)

class shift_1(unittest.TestCase):
    def test_1_shift_encode(self):
        a = obj.encode('z')
        self.assertEqual(a, 'A')

    def test_shift_decode(self):
        a = obj2.decode('a')
        self.assertEqual(a, 'Y')

class shift_2(unittest.TestCase):
    def test_2_shift_encode(self):
        a = obj2.encode('z')
        self.assertEqual(a, 'B')

    def test_2_shift_decode(self):
        a = obj2.decode('a')
        self.assertEqual(a, 'Y')

class shift_1_for_abc(unittest.TestCase):
    def test_2_shift_encode(self):
        a = obj.encode('abc')
        self.assertEqual(a, 'BCD')

    def test_2_shift_decode(self):
        a = obj.decode('abc')
        self.assertEqual(a, 'ZAB')

