class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        non_zero=[]
        zero=[]
        for i in nums:
            if i==0:
                zero.append(i)
            else:
                non_zero.append(i)
        result= non_zero+zero
        for i in range(len(nums)):
            nums[i]=result[i]
        