def maximumWealth(accounts):
    max_wealth=0
    for i in accounts:
        sum=0
        for j in i:
            sum=sum+j
        max_wealth=max(max_wealth,sum)
    return max_wealth
accounts=[[1,2,3],[4,5,6]]
print(maximumWealth(accounts))