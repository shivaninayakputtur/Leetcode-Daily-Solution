from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        non_zero = []
        zero = []
        for i in nums:
            if i == 0:
                zero.append(i)
            else:
                non_zero.append(i)
        result = non_zero + zero
        for i in range(len(nums)):
            nums[i] = result[i]
nums = [0, 1, 0, 3, 12]
obj = Solution()
obj.moveZeroes(nums)
print(nums)