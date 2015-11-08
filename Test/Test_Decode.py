__author__ = 'Tom'
import unittest
import sys
# Add the ptdraft folder path to the sys.path list
sys.path.append('/Users/Tom/PycharmProjects/vector_class/Vector_Calc_py')
from index import a

class Test_Error_Unequal_Length(unittest.TestCase):

    def test_raiseError_for_unequal_length(self):
        self.assertRaises(AttributeError, lambda: short.norm(a))

print(a)