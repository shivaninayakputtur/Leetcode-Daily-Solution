def createTargetArray(nums,index):
        target=[]
        for i in range(len(nums)):
            target.insert(index[i],nums[i])
        return target
nums=[0,1,2,4,3]
index=[1,2,2,3,6]
print(createTargetArray(nums,index))