def getConcatenation(nums):
    result=[]
    for i in nums:
        result=nums+nums
    return result
nums=[1,2,3]
print(getConcatenation(nums))