#/usr/bin/env python3



class Sum2Num:
    def solve(self, nums, target):
        for index, num in enumerate(nums):
            diff = target - num
            if diff in nums[index:]:
                return [index, nums.index(diff)]
        return None
print(Sum2Num().solve([2, 11, 15, 7], 9))
