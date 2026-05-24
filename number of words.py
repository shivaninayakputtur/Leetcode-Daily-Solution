def mostWordsFound(sentences):
    max_word=0
    for sentence in sentences:
        words=len(sentence.split())
        max_word=max(max_word,words)
    return max_word
sentences=("alisa and bob love lc","pressure is privilage" )
print(mostWordsFound(sentences))