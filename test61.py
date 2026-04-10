class Solution:
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))
s=Solution()
nums=[1,2,3,1]
print(s.containsDuplicate(nums))