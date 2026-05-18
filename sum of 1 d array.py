def runningSum(nums):
    result=[]
    sum=0
    for i in nums:
        sum=sum+i
        result.append(sum)
    return result
nums=[1,2,3,4,5]
print(runningSum(nums))