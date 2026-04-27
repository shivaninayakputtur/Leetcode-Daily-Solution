class Solution:
    def missingNumber(self, nums):
        total = sum(range(len(nums)+1))
        return total-sum(nums)
nums=[3,0,1]    
obj=Solution()
print(obj.missingNumber(nums))