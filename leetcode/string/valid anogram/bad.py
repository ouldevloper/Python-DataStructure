class Solve:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

    def solve(self):
        hashmap1 = {}
        hashmap2 = {}
        if len(self.str1) != len(self.str2):
            return False
        for c1, c2 in zip(self.str1, self.str2):
            if c1 in hashmap1:
                hashmap1[c1] += 1
            else:
                hashmap1[c1]  = 1
            
            if c2 in hashmap2:
                hashmap2[c2] += 1
            else:
                hashmap2[c2]  = 1

        for c1, c2 in zip(self.str1, self.str2):
            if c1 not in hashmap1 or c1 not in hashmap2:
                return False
            if c2 not in hashmap1 or c2 not in hashmap2:
                return False
            if hashmap1[c1] != hashmap2[c1] or hashmap1[c2] != hashmap2[c2]:
                return False
        return True
        
print(Solve('abc0cd','abc1cd').solve())