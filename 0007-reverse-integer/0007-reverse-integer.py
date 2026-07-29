class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        if x<0: 
            negative=True
        else:
            negative=False
        x=abs(x)
        rev=int(str(x)[::-1])
        if negative:
            rev=-rev
        if rev > 2**31 - 1 or rev < -2**31:
            return 0
        return rev

