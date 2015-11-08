__author__ = 'Tom'
import unittest
import sys
# Add the ptdraft folder path to the sys.path list
sys.path.append('/Users/Tom/PycharmProjects/vector_class/Vector_Calc_py')

from CaesarCipher_py import index

obj = index.CaesarCipher(1)

obj2 = index.CaesarCipher(3)

class encoding(unittest.TestCase):
    def test_1_shift_encode(self):
        a = obj.encode('z')
        self.assertEqual(chr(a[0]), 'a')


class decoding(unittest.TestCase):
    def test_1_shift_decode(self):
        a = obj.encode('z')
        self.assertEqual(chr(a[0]), 'a')


class toOrd(unittest.TestCase):
    def test_(self):
        self.assertEqual(str(a), '(1,2,3)')


class toChr(unittest.TestCase):
    def test_(self):
        self.assertEqual(str(a), '(1,2,3)')
