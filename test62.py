class Solution:
    def missingNumber(self, nums):
        total = sum(range(len(nums)+1))
        return total - sum(nums)
s=Solution()
nums=[1,0,3]
print(s.missingNumber(nums))   
