class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        max_candy = max(candies)
        for i in candies:
            if i + extraCandies >= max_candy:
                result.append(True)
            else:
                result.append(False)
        return result 