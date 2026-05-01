class Solution:
    def kidsWithCandies(self, candies):
        max_candies=max(candies)
        result=[]
        for c in candies:
            if c+3>=max_candies:
                result.append(True)
            else:
                result.append(False)
        return result
obj=Solution()
candies=[2,3,5,1,3]
print(obj.kidsWithCandies(candies))