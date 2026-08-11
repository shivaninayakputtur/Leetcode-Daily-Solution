class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum=0
        product=1
        for char in str(n):
            digit=int(char)
            sum+=digit
            product=product*digit
        return product-sum