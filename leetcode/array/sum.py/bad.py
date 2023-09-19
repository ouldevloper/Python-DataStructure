#/usr/bin/env python3


nums = [
            1,4,2,5,7,3,7,9,4,65,87,435,876,3456,3453,4567,46,374563,
            456,3456,3456,3456345,6345,634,563,456,345,63,456,3456,
            3456,3,47563,456,345,63,456,3456,345,63,456,347563495,6345,
            63,456,345,63,45,634,56,34,56,345,63,465,3456,34,56,34,
            563,45763,13456,345,634,563,45363,4563,456,3456,345,63456
        ]
class Sum2Num:
   
    def solve(self, nums, target):
        for index, num in enumerate(nums):
            for index2, num2 in enumerate(nums[index:]):
                if num+num2 == target:
                    return [index, index2]

        return None
print(Sum2Num().solve(nums, 3456345+4563))
