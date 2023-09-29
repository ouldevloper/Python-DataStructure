#/usr/bin/env python3

class NumOf1Bits:
    def getnums(self, num)->int:
        if num <0:
            print('number should be an unisigned number')
            return
        count = 0
        for i in range(32):
            mask = 2 ** i # 1 << i
            # print('mask: ', mask)
            # print('num & mask: ', num & mask)
            if (num & mask) != 0:
                count+=1
        return count


print(NumOf1Bits().getnums(1000))
