def HeightsCheck(heights):
    count=0
    x=sorted(heights)
    for i in range(len(heights)):
        if heights[i]!=x[i]:
            count+=1
            return count
heights=[5,4,3,2,1]
print(HeightsCheck(heights))