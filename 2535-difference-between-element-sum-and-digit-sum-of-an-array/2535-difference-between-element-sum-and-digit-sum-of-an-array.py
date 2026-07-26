class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum=0
        sum1=0
        for i in nums:
            sum=sum+i
            for digit in str(i):
                sum1=sum1+int(digit)
        return abs(sum-sum1)