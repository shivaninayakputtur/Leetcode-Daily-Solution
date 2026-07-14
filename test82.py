def maximizeSum(nums,k):
        max_num = max(nums)
        result = 0
        for i in range(k):
            result += max_num
            max_num += 1
        return result
nums=[1,2,3,4,5]
k=3
print(maximizeSum(nums,k))
