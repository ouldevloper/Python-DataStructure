#!/usr/bin/env python


class Anogram:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2


    def solve(self)->bool:
        if len(self.str1) != len(self.str2): return False
        map = [0]*26
        for s1, s2 in zip(self.str1, self.str2):
            map[ord('a')-ord(s1)]+=1
            inxd = ord('a')-ord(s2)
            if map[inxd]>0:
                map[inxd] -= 1
        print(map)
        return sum(map) == 0

print(Anogram('b', 'a').solve())