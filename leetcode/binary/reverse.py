#!/usr/bin/env python 



class Reverse:
    def __init__(self, number):
        rev = 0
        for i in range(1, 33):
            rev <<= 1
            rev  |= (1&number)
            print(rev, bin(rev), number, bin(number))
            number >>= 1
        print(rev)


Reverse(123)