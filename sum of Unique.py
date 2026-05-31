def SumOfUnique(nums):
    sum=0
    for num in nums:
        if nums.count(num)==1:
            sum=sum+num
    return sum
nums=[1,2,3,2]
print(SumOfUnique(nums))