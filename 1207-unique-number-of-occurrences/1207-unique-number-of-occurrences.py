class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        counts = list(d.values())
        for c in counts:
            if counts.count(c) > 1:
                return False
        return True