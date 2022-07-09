#!/usr/bin/env python3


def facturial(num):
    if num == 0: return 1
    else: return num*facturial(num-1)
    
    
print(facturial(5))