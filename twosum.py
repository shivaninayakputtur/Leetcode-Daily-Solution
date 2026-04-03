class solution:
    def twoSum(self, nums,target):
        for i in range(len(nums)):
         for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return[i,j]
obj=solution()
result=obj.twoSum([2,7,8,9],9)
print(result)