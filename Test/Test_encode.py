__author__ = 'Tom'
import unittest
import sys
# Add the ptdraft folder path to the sys.path list
sys.path.append('/Users/Tom/PycharmProjects/vector_class/Vector_Calc_py')

from index import a, b
from index import Vector


class __init__(unittest.TestCase):
    def test_length_property(self):
        self.assertEqual(a.length, 3)

class __str__(unittest.TestCase):
    def test_(self):
        self.assertEqual(str(a), '(1,2,3)')

class Add(unittest.TestCase):
    def test_returns_vector_object(self):
        vec1 = a.add(a)
        self.assertEqual(vec1.__class__.__name__, 'Vector')

    def test_adds_properly(self):
        vec2 = a.add(a)
        self.assertEqual(vec2.array, [4, 6, 8])

class Subtract(unittest.TestCase):
    pass


class Norm(unittest.TestCase):
    pass


class Dot(unittest.TestCase):
    pass