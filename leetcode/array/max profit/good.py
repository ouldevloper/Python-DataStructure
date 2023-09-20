#/usr/bin/env python


# [7, 1, 5, 3, 6, 4]
class MaxProfit:
    def solve(self, arry):
        profit = 0
        left   = 0
        for i in range(1, len(arry)):
            if arry[i] > arry[left]:
                p = arry[i] - arry[left] 
                if p>profit:
                    profit = p
            else:
                left = i
            #print('[-] ', ' left:', left, ' | right:',i, ' | profit: ', profit)
        return profit

tests = [
    [7, 1, 5, 3, 6, 4],
    [7, 6, 4, 3, 1]
]
t = MaxProfit()
for i in tests:
    print('test: ',t.solve(i))