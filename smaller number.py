def smallerNumbersThanCurrent(nums):
        result=[]
        for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    count+=1
            result.append(count)
        return result
nums=[8,3,2,1]
print(smallerNumbersThanCurrent(nums))