#/usr/bin/env python3


class Sum2Nums:
    def __init__(self):
        pass
    

    def getSum(self, num1, num2)->int:
        while num2 != 0:
            # print()
            carry = 0
            # print("num1: %d, num2: %d, carry: %d, \n"%(num1, num2, carry))
            carry = num1 & num2
            # print("num1: %d, num2: %d, carry: %d, \n"%(num1, num2, carry))
            num1 ^= num2
            # print("num1: %d, num2: %d, carry: %d, \n"%(num1, num2, carry))
            num2 = carry << 1
            # print("num1: %d, num2: %d, carry: %d, \n"%(num1, num2, carry))
            # print()
        return num1

print (Sum2Nums().getSum(10, 10))
