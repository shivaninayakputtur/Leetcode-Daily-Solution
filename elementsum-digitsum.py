def differenceOfSum(nums):
    sum=0
    sum1=0
    for i in nums:
        sum=sum+i
        for digit in str(i):
            sum1=sum1+int(digit)
    return abs(sum-sum1)
nums=[1,15,6,4]
print(differenceOfSum(nums))