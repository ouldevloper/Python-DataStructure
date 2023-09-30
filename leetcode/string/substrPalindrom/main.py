#!/usr/bin/env python3
import ctypes


class SubString:
    def __init__(self, str):
        self.str = str
        self.isAlphaRange = range(26)
        self.nums         = range(10)
    def isAlpha(self, char)->bool:
        return (ord(char)-ord('a')) in self.isAlphaRange or (ord(char)-ord('0')) in self.nums
    
    def solve(self)->bool: 
        left = 0
        right = len(self.str)-1
        isPalindrom = True
        while right>left:
            if not self.isAlpha(self.str[left]):
                left+=1
            elif not self.isAlpha(self.str[right]):
                right-=1
            else:
                if self.str[left] != self.str[right]:
                    isPalindrom = False
                    break
                left+=1
                right-=1
        return isPalindrom
            
print(SubString('1, 2192,,,,,,,,,,,,,,,,,,,,,1').solve())