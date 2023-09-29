#!/usr/bin/env python 



class Reverse:
    def __init__(self, number):
        rev = 0
        for i in range(32):
            rev <<= 1
            rev  |= (1&number)
            number >>= 1
        print(rev)


Reverse(123)