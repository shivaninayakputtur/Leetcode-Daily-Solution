class Solution:
    def finalValueAfterOperations(self, operations):
        x=0 #counter
        for op  in operations:
            if "++"in op:
                x=x+1
            else:
                x=x-1
        return x
obj=Solution()
operations=["--x","x++","++x"]
print(obj.finalValueAfterOperations(operations))