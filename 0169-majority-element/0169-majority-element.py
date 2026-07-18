class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        max_i=0
        max_count=0
        for i in nums:
            if i in d:
                d[i]=d[i]+1
            else:
                d[i]=1
            if d[i] > max_count:
                max_count=d[i]
                max_i=i
        return max_i