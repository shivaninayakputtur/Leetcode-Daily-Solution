def mergeAlternately(word1,word2):
    result=""
    for i in range(min(len(word1),len(word2))):
        result+=word1[i]+word2[i]
    result+=word1[i+1:]+word2[i+1:]
    return result
word1="abc"
word2="pqr"
print(mergeAlternately(word1,word2))