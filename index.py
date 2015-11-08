__author__ = 'Tom'
import math

class CaesarCipher(object):
    def __init__(self, shift):
        self.shift = shift

    def encode(self, str):
        shifted = [self.map_encode(x, self.shift) for x in str]
        return shifted

    def decode(self, str):
        unshifted = [self.map_decode(x, self.shift) for x in str]
        return unshifted

    def map_encode(self, char, shift):
        shifted = ord(char) + self.shift
        if int(shifted) > 122:
            shifted = (shifted - 1) - 122 + 97
        return shifted

    def map_decode(self, char, shift):
        shifted = ord(char) - self.shift
        if shifted < 97:
            shifted =  122 - (97 - (shifted - self.shift) )
        return shifted

a = CaesarCipher(2)


c = a.decode('a')


print(chr(c[0]))
