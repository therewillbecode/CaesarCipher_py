__author__ = 'Tom'
import math

class CaesarCipher(object):
    def __init__(self, shift):
        self.shift = shift

    def encode(self, str):
        print(str)
        str = str.lower()
        shifted = [chr(self.map_encode(x, self.shift)) for x in str]
        return ''.join(shifted).upper()

    def decode(self, str):
        str = str.lower()
        print(str)
        unshifted = [chr(self.map_decode(x, self.shift)) for x in str]
        return ''.join(unshifted).upper()

    def map_encode(self, char, shift):
        shifted = ord(char) + self.shift
        if int(shifted) > 122:
            shifted = (shifted - 1) - 122 + 97
        return shifted

    def map_decode(self, char, shift):
        shifted = ord(char) - self.shift
        if shifted < 97:
            shifted = 122 - (97 - (shifted + 1))
        return shifted

a = CaesarCipher(5)

c = a.encode('NY,X%F%XMNKY%HNUMJW&&')

// " NY'X F XMNKY HNUMJW!! "
print(c)
