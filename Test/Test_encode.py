__author__ = 'Tom'
import unittest
import sys
# Add the ptdraft folder path to the sys.path list
sys.path.append('/Users/Tom/PycharmProjects/vector_class/Vector_Calc_py')

from CaesarCipher_py import index

obj = index.CaesarCipher(1)

obj2 = index.CaesarCipher(2)

class shift_1(unittest.TestCase):
    def test_1_shift_encode(self):
        a = obj.encode('z')
        self.assertEqual(chr(a[0]), 'a')

    def test_1_shift_decode(self):
        a = obj2.encode('z')
        self.assertEqual(chr(a[0]), 'a')

class shift_2(unittest.TestCase):
    def test_2_shift_encode(self):
        a = obj.encode('z')
        self.assertEqual(chr(a[0]), 'b')

    def test_2_shift_decode(self):
        a = obj2.decode('a')
        self.assertEqual(chr(a[0]), 'y')

class toOrd(unittest.TestCase):
    def test_(self):
        self.assertEqual(str(a), '(1,2,3)')


class toChr(unittest.TestCase):
    def test_(self):
        self.assertEqual(str(a), '(1,2,3)')
