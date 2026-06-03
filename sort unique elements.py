def sortPeople(names,heights):
        pairs = list(zip(names, heights))
        sorted_pairs = sorted(pairs, key=lambda x: x[1], reverse=True)
        return [name for name, height in sorted_pairs]
names=["mary","raju","kiran"]
heights=[108,180,153]
print(sortPeople(names,heights))